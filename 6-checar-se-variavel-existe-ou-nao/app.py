nome = "Lucas"

#Escopo local
if 'nome' in locals():
    print('A variável está em escopo local')
if 'idade' in locals():
    print('A variável NÃO está em escopo local')

#Escopo global
if 'nome' in globals():
    print('A variável está em escopo global')  