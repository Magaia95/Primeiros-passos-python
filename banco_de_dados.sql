from dataclasses import dataclass, field
from datetime import datetime
import pyotp
import qrcode


# 1. Modelo de Dados para Simular o Banco de Dados
@dataclass
class UserMock:
    id: int
    email: str
    password_hash: str  # Simulação de hash de senha
    two_factor_secret: str = field(default_factory=pyotp.generate_base32)
    is_2fa_enabled: bool = False


# 2. Repositório em Memória (Mock Database)
class MockUserRepository:
    def __init__(self):
        # Base de dados simulada com dados pré-carregados
        self._db: dict[int, UserMock] = {
            1: UserMock(
                id=1,
                email="dev.teste@empresa.com",
                password_hash="pbkdf2:sha256:mock_hash_123",
            ),
            2: UserMock(
                id=2,
                email="qa.usuario@empresa.com",
                password_hash="pbkdf2:sha256:mock_hash_456",
                is_2fa_enabled=True,
            ),
        }

    def get_by_id(self, user_id: int) -> UserMock | None:
        return self._db.get(user_id)

    def get_by_email(self, email: str) -> UserMock | None:
        return next((u for u in self._db.values() if u.email == email), None)

    def update_2fa_status(self, user_id: int, enabled: bool) -> bool:
        user = self.get_by_id(user_id)
        if user:
            user.is_2fa_enabled = enabled
            return True
        return False


# 3. Serviço de 2FA
class TwoFactorAuthService:
    def __init__(self, repo: MockUserRepository, app_name: str = "MinhaAPI"):
        self.repo = repo
        self.app_name = app_name

    def setup_2fa(self, user_id: int):
        """Gera a URI TOTP e o QR Code em terminal/arquivo para setup no app."""
        user = self.repo.get_by_id(user_id)
        if not user:
            raise ValueError("Usuário não encontrado.")

        # Criar URI no padrão TOTP (otpauth://totp/...)
        totp = pyotp.TOTP(user.two_factor_secret)
        provisioning_uri = totp.provisioning_uri(
            name=user.email, issuer_name=self.app_name
        )

        # Opcional: Gerar QR Code no terminal para escaneamento rápido
        qr = qrcode.QRCode()
        qr.add_data(provisioning_uri)
        print(f"\n--- QR Code para Setup de 2FA ({user.email}) ---")
        qr.print_ascii(invert=True)

        return {
            "secret": user.two_factor_secret,
            "provisioning_uri": provisioning_uri,
        }

    def verify_and_enable(self, user_id: int, code: str) -> bool:
        """Valida o código de 6 dígitos gerado pelo app autenticador."""
        user = self.repo.get_by_id(user_id)
        if not user:
            return False

        totp = pyotp.TOTP(user.two_factor_secret)

        # valid_window=1 permite tolerância de ±30 segundos caso haja descompasso de relógio
        if totp.verify(code, valid_window=1):
            self.repo.update_2fa_status(user_id, enabled=True)
            return True
        return False


# --- Demonstration of Usage ---
if __name__ == "__main__":
    db = MockUserRepository()
    auth_service = TwoFactorAuthService(db)

    # Buscar usuário do Mock DB
    user = db.get_by_id(1)
    print(f"Usuário selecionado: {user.email}")
    print(f"Segredo Base32 (Mock): {user.two_factor_secret}")

    # 1. Configurar 2FA (Exibe QR Code no terminal)
    setup_info = auth_service.setup_2fa(user.id)

    # 2. Simular geração de token no lado do cliente (App do Usuário)
    totp_client = pyotp.TOTP(user.two_factor_secret)
    current_token = totp_client.now()
    print(f"\nCódigo TOTP Gerado Atualmente: {current_token}")

    # 3. Testar verificação da API
    is_valid = auth_service.verify_and_enable(user.id, current_token)
    print(f"Validação do token: {'SUCESSO' if is_valid else 'FALHA'}")
    print(f"Status 2FA do usuário no Mock DB: {user.is_2fa_enabled}")
