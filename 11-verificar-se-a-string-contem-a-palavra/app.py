frase = "O rato roeu a roupa do rei de Roma"

# print(frase)

palavra = "Rato"

# if palavra.lower() not in frase:
#     print(f"A palavra {palavra} não existe na frase - {frase} -")
# else:
#     print(f"A frase - {frase} - contém a palavra -{palavra}-")    


#Alternativa
if frase.count(palavra.lower()) == 0:
    print(f"A palavra -{palavra}- não existe na frase - {frase} -")
else:
    print(f"A frase - {frase} - contém a palavra -{palavra}-")    
    