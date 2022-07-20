import os #auxilia com diretórios e arquivos
import pathlib
from pathlib import Path

# if os.path.isdir("diretorio"):
#     print('O diretório existe')
# else:
#     print('O diretorio não existe')    



#alternativa usando a lib -pathlib-
if Path('x').is_dir():
    print('O diretório existe')
else:
    print("O diretório não existe")    