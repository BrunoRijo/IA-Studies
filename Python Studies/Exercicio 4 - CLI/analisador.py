# Criar um utilitário de terminal simples com argparse que receba o caminho de um arquivo como parâmetro
# para executar deve-se digitar no terminar da pasta que possui esse arquivo "python analisador.py (nome do arquivo)"

import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Minha primeira CLI para checar arquivos.")
    parser.add_argument("caminho", help="O caminho completo ou relativo do arquivo")

    args = parser.parse_args()
    caminho_do_arquivo = args.caminho

    print(f"Analisando: {caminho_do_arquivo}...")

    if os.path.exists(caminho_do_arquivo):
        tamanho = os.path.getsize(caminho_do_arquivo)
        print(f"✓ Arquivo encontrado com sucesso! Tamanho: {tamanho} bytes.")
    else:
        print("✗ Erro: O arquivo informado não existe.")

if __name__ == "__main__":
    main()