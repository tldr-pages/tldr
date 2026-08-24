# yt-dlp

> Um fork do youtube-dl com novas funções e correções.
> Baixe videos do YouTube e outros sites.
> Veja também: `ytfzf`.
> Mais informações: <https://github.com/yt-dlp/yt-dlp#usage-and-options>.

- Baixa um video ou playlist (com as opções padrão do comando abaixo):

`yt-dlp "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Lista os formatos disponíveis para download de um vídeo:

`yt-dlp {{[-F|--list-formats]}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Baixa um vídeo ou playlist usando o melhor vídeo MP4 disponível (o padrão é "bv\*+ba/b"):

`yt-dlp {{[-f|--format]}} "{{bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]}}" "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Extrai o áudio de um vídeo (requer ffmpeg ou ffprobe):

`yt-dlp {{[-x|--extract-audio]}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Especifica o formato e a qualidade do áudio extraido (entre 0 (maior qualidade) e 10 (menor qualidade), padrão = 5):

`yt-dlp {{[-x|--extract-audio]}} --audio-format {{mp3}} --audio-quality {{0}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Baixa apenas o segundo, quarto, quinto, sexto e último item de uma playlist (o primeiro item é 1, e não 0):

`yt-dlp {{[-I|--playlist-items]}} 2,4:6,-1 "{{https://youtube.com/playlist?list=PLbzoR-pLrL6pTJfLQ3UwtB-3V4fimdqnA}}"`

- Baixa todas as playlists de um canal/usuário do YouTube mantendo cada playlist em um diretório separado:

`yt-dlp {{[-o|--output]}} "{{%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s}}" "{{https://www.youtube.com/user/TheLinuxFoundation/playlists}}"`

- Baixa um curso da Udemy mantendo cada capítulo em um diretório separado:

`yt-dlp {{[-u|--username]}} {{usuário}} {{[-p|--password]}} {{senha}} {{[-P|--paths]}} "{{caminho/para/diretório}}" {{[-o|--output]}} "{{%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s}}" "{{https://www.udemy.com/java-tutorial}}"`
