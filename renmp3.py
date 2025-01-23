import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

def renomear_arquivos_mp3(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".mp3"):
            caminho_arquivo = os.path.join(pasta, arquivo)
            try:
                # Tenta ler as tags ID3 do arquivo
                mp3 = EasyID3(caminho_arquivo)
                artista = mp3.get('artist', ['Desconhecido'])[0]
                titulo = mp3.get('title', ['Desconhecido'])[0]
                
                # Cria o novo nome no formato ARTISTA - NOME DA MÚSICA
                novo_nome = f"{artista} - {titulo}.mp3"
                novo_caminho = os.path.join(pasta, novo_nome)

                # Renomeia o arquivo
                os.rename(caminho_arquivo, novo_caminho)
                print(f"Arquivo renomeado para: {novo_nome}")

            except ID3NoHeaderError:
                print(f"Tag ID3 não encontrada no arquivo: {arquivo}")
            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo}: {e}")

# Defina o caminho da pasta onde estão os arquivos MP3
pasta_mp3 = "D:\MP3\NAC\MUKIFO\TEMP"

renomear_arquivos_mp3(pasta_mp3)
