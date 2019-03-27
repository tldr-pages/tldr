# eyeD3

> Lê e manipula os metadados de arquivos MP3.
> Página oficial: <https://eyed3.readthedocs.io/en/latest/>.

- Visualiza as informações de um arquivo MP3:

`eyeD3 {{filename.mp3}}`

- Define o título de um arquivo MP3:

`eyeD3 --title {{"A Title"}} {{filename.mp3}}`

- Define o álbum de todos os arquivos MP3 de um diretório:

`eyeD3 --album {{"Album Name"}} {{*.mp3}}`

- Define a capa do álbum para um arquivo MP3:

`eyeD3 --add-image {{front_cover.jpeg}}:FRONT_COVER: {{filename.mp3}}`
