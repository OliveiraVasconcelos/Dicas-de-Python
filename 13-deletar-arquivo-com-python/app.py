import os 

if os.path.exists("arquivoTeste.txt"): #os.path.isdir("arquivoTeste") -no caso de querer remover uma pasta e não um arquivo-
    os.remove("arquivoTeste.txt")
    print("Arquivo removido com sucesso")
    
else:
    print("Arquivo inexistente...")    