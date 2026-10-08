import random
import string

# Dados simulados do utilizador
email_registado = "usuario@gmail.com"
telefone_registado = "841234567"

print("=============================================")
print("--- SISTEMA DE GERENCIAMENTO COM 2FA ---")
print("=============================================")

# --- FASE 1: VALIDAÇÃO DE IDENTIDADE INICIAL (2FA) ---
print("\n[PASSO 1] Autenticação de Segurança Necessária.")
opcao_2fa = input("Onde deseja receber o código de autenticação? (1 - E-mail / 2 - Telefone): ").strip()

if opcao_2fa in ['1', '2']:
    destino = email_registado if opcao_2fa == '1' else telefone_registado
    meio = "e-mail" if opcao_2fa == '1' else "número de telefone"
    
    codigo_autenticacao = str(random.randint(100000, 999999))
    print(f"\n[SISTEMA] Código enviado para o seu {meio}: {destino}")
    print(f"[SIMULAÇÃO] Seu código de verificação é: {codigo_autenticacao}")
    
    validacao = input("\nDigite o código de 6 dígitos recebido: ").strip()
    
    if validacao != codigo_autenticacao:
        print("\n[ERRO] Código incorreto! Acesso negado por segurança.")
        exit()
    else:
        print("\n[OK] Identidade confirmada com sucesso!")
else:
    print("\nOpção inválida. Sessão encerrada.")
    exit()

# --- FASE 2: GERAR SENHA AUTOMÁTICA E OPÇÃO DE TROCA ---
print("\n---------------------------------------------")
print("[PASSO 2] Configuração de Senha")
caracteres = string.ascii_letters + string.digits + string.punctuation
senha_gerada = "".join(random.choice(caracteres) for _ in range(14))

print(f"[SISTEMA] Senha de 14 caracteres gerada automaticamente: {senha_gerada}")

trocar = input("\nDeseja trocar esta senha gerada por uma da sua escolha? (s/n): ").strip().lower()

if trocar == 's':
    while True:
        nova_senha = input("Digite a sua nova senha (mínimo 8, máximo 14 caracteres): ").strip()
        if 8 <= len(nova_senha) <= 14:
            senha_atual = nova_senha
            print("-> Sua senha personalizada foi guardada com sucesso!")
            break
        else:
            print(f"Tamanho inválido! A senha tem {len(nova_senha)} caracteres. Deve ter entre 8 e 14.")
else:
    senha_atual = senha_gerada
    print("-> Mantendo a senha gerada pelo programa.")

# --- FASE 3: TENTATIVAS DE LOGIN (MÁXIMO 3) ---
print("\n---------------------------------------------")
print("[PASSO 3] Tela de Login")

tentativas_restantes = 3
acesso_concedido = False

while tentativas_restantes > 0:
    senha_digitada = input(f"\nDigite a sua senha para entrar (Tentativas restantes: {tentativas_restantes}): ").strip()
    
    if senha_digitada == senha_atual:
        print("\n=== LOGIN EFETUADO COM SUCESSO! BEM-VINDO AO SISTEMA ===")
        acesso_concedido = True
        break
    else:
        tentativas_restantes -= 1
        if tentativas_restantes > 0:
            print("Senha incorreta. Tente novamente!")

# --- FASE 4: BLOQUEIO E DESBLOQUEIO DE CONTA ---
if not acesso_concedido:
    print("\n--------------------------------------------------")
    print("[ALERT] Número máximo de tentativas atingido! CONTA BLOQUEADA.")
    
    desbloquear = input("\nDeseja desbloquear a conta via verificação de segurança? (s/n): ").strip().lower()
    
    if desbloquear == 's':
        opcao_recuperacao = input("Enviar código de desbloqueio para: (1 - E-mail / 2 - Telefone): ").strip()
        
        if opcao_recuperacao in ['1', '2']:
            destino = email_registado if opcao_recuperacao == '1' else telefone_registado
            codigo_desbloqueio = str(random.randint(100000, 999999))
            
            print(f"\n[SISTEMA] Código de desbloqueio enviado: {codigo_desbloqueio}")
            confirmacao = input("Digite o código de 6 dígitos para desbloquear: ").strip()
            
            if confirmacao == codigo_desbloqueio:
                print("\n[SUCESSO] Conta desbloqueada com sucesso!")
                
                # Permite redefinir a senha para voltar a ter acesso
                while True:
                    nova_senha = input("Crie uma NOVA senha (mínimo 8, máximo 14 caracteres): ").strip()
                    if 8 <= len(nova_senha) <= 14:
                        senha_atual = nova_senha
                        print(f"Nova senha guardada: {senha_atual}")
                        print("Você já pode fazer login normalmente na próxima sessão!")
                        break
                    else:
                        print(f"Tamanho inválido! A senha tem {len(nova_senha)} caracteres.")
            else:
                print("\n[ERRO] Código de desbloqueio incorreto. A conta permanece bloqueada.")
        else:
            print("Opção inválida. Processo encerrado.")
    else:
        print("Sessão encerrada. A conta continua bloqueada.")
