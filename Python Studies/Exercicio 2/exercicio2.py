from pathlib import Path
#Exercício: Escrever um script para abrir um arquivo (.pas ou .txt) usando open() 
#           e salvar apenas linhas específicas em um novo arquivo

FILENAME = "NovoArquvo.txt"

file = Path(FILENAME)

def command():
  return "a" if file.exists else "w"   

def WriteInFile(content):
  with open(FILENAME, command()) as file:
    file.write(content)
                  
#Salvar em outro arquivo apenas as linhas que contêm TODO.
with open("ArquivoExemplo.pas", "r") as PascalFile:
    for line in PascalFile:
        if "TODO" in line:
          WriteInFile(line)

with open(FILENAME, "r") as NewFile:
   contentInside = NewFile.read()
   print(contentInside)