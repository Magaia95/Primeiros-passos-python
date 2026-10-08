import random
import string

print("--- BEM-VINDO AO SEU GERADOR DE SENHAS ---")

# 1. Perguntar o tamanho da senha que você deseja
tamanho = int(input("Quantos caracteres você quer na sua senha? (Ex: 12): "))

# 2. Juntar os ingredientes da senha (letras, números e símbolos)
caracteres_disponiveis = string.ascii_letters + string.digits + string.punctuation

# 3. Misturar tudo e escolher os caracteres aleatoriamente
senha_gerada = "".join(random.choice(caracteres_disponiveis) for i in range(tamanho))

# 4. Mostrar o resultado na tela
print("\nSua senha segura foi gerada com sucesso!")
print(f"-> {senha_gerada} <-")
print("------------------------------------------")
