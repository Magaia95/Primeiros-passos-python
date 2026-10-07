usuario="algerio"
idade=31
status_ativo=True
print(f"usuario:{usuario}|Idade {idade}aos|ativo{status_ativo}")
if idade>=31 and status_ativo==True:
  print("Acesso Permitido!")
else:
  print("acesso Negado!")

    nome_aluno="algerio"
nota=12.7
presenca=True
if nota>= 7 and presenca:
  print(f"aluno{nome_aluno}aprovado com nota {nota}!")
else:
  print(f"aluno {nome_aluno} precisa de recuperacao.")

valor_compra=150
eh_vip=False
if valor_compra>=100 or eh_vip:
  print("Desconto aplicado com sucesso!")
else:
print("sem desconto. Valor normal aplicado.")

idade_atleta=15
if idade_atleta<12:
  print("categoria:infantil")
elif idade_atleta<18:
print("categoria:juvenil")
else:
  print("categoria: adulto")

  for numero in range(1,6):
  print(f"contagem:{numero}")

frutas=["maca", "banana", "laranja"]
  for fruta in frutas:
    print(f"Eu gosto de {fruta}")

contador=1
while contador<=3:
  print(f"contador com while: {contador}")
contador=contador+1


def dar_boas_vindas (nome):
  print(f"Ola, {nome}! Seja bem_vindo ao python.")
dar_boas_vindas("Algerio")
