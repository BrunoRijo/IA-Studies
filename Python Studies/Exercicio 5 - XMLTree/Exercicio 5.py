#Essa atividade consiste em 
# Utilizar xml.etree.ElementTree para ler múltiplos arquivos XML 
# e consolidar suas tags em um único documento estruturado.

import os
import xml.etree.ElementTree as ET

diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_diretorio = os.path.join(diretorio_script, "arquivosXML")

if os.path.exists(caminho_diretorio) and os.path.isdir(caminho_diretorio):
  conteudo = os.listdir(caminho_diretorio) 
  ficheiros_xml = []

  #isola apenas os arquivos .xml da pasta informada
  for item in conteudo:
      caminho_completo = os.path.join(caminho_diretorio, item)
      
      if os.path.isfile(caminho_completo) and item.lower().endswith('.xml'):
          ficheiros_xml.append(caminho_completo)

  #percorre a lista de arquivos XML para separar as tags e criar um novo arquivo a partir disso.
  novo_arquivo = ET.Element("pedidos")
  for arquivo in ficheiros_xml:
    tree = ET.parse(arquivo)
    root = tree.getroot()
    lista_de_pedidos = root.findall("pedido")

    for pedido in lista_de_pedidos:
        novo_arquivo.append(pedido)

  #salva o arquivo novo consolidado.
  arquivo_final = ET.ElementTree(novo_arquivo)
  arquivo_final.write(os.path.join(diretorio_script, "meu_pedido.xml"), encoding="utf-8", xml_declaration=True)

  print("Arquivo salvo com sucesso!")
else:
  print("diretório não encontrado!")



