#Usuário pode ou não ter a CNH

cnh = True
idade = int(input("Digite sua idade: "))
idadeBase = 18

if (idade >= idadeBase) and (cnh == True):
    print("Você está autorizado a conduzir um automóvel")
else:
    print("Lamento. Você não está autorizado a dirigir um automóvel.")    