from pickletools import read_int4


tupla = (('valor', 'chave'), ('nome', 'Lucas'), ('idade',30))

dicionario = dict((chave,valor) for chave,valor in tupla) #método dict usado para transformar os valores

print(dicionario)