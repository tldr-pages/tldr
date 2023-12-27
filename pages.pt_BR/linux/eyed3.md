# eyeD3

> Lê e manipula os metadados de arquivos MP3.
> Mais informações: <https://eyed3.readthedocs.io>.

- Visualiza as informações de um arquivo MP3:

`eyeD3 {{arquivo.mp3}}`

- Define o título de um arquivo MP3:

`eyeD3 --title "{{titulo}}" {{arquivo.mp3}}`

- Define o álbum de todos os arquivos MP3 de um diretório:

`eyeD3 --album "{{nome_do_album}}" {{*.mp3}}`

- Define a capa do álbum para um arquivo MP3:

`eyeD3 --add-image {{capa.jpeg}}:FRONT_COVER: {{arquivo.mp3}}`
