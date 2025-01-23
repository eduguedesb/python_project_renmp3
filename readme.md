# Visão Geral:
Este script automatiza o processo de renomeação de arquivos MP3 com base nas informações de metadados ID3. Ele percorre uma pasta especificada, lê as tags de artista e título de cada arquivo MP3 e os renomeia no formato ARTISTA - NOME DA MÚSICA.mp3. Caso um arquivo não tenha as tags ID3 ou ocorram erros, o script exibe uma mensagem informativa.

# Funcionamento:
Lê as tags ID3 (artista e título) de arquivos MP3 usando a biblioteca mutagen.
<br>
Renomeia os arquivos MP3 no formato ARTISTA - NOME DA MÚSICA.mp3.
<br>
Lida com exceções caso o arquivo não contenha metadados ID3 ou ocorram outros erros durante o processo.
<br>
Exibe uma mensagem de sucesso ou erro para cada arquivo processado.

# Dependências:
mutagen: Biblioteca usada para acessar e manipular os metadados ID3 dos arquivos MP3.

# Como Usar:
Defina o caminho da pasta contendo os arquivos MP3 no código.
<br>
Execute o script com o seguinte comando: py renmp3.py ou python renmp3.py.

# Observações:
Se os metadados artista ou título não estiverem presentes, o script utiliza "Desconhecido" como valor padrão.
<br>
Caso o arquivo MP3 não possua tags ID3, ele será ignorado e uma mensagem será exibida no console.
