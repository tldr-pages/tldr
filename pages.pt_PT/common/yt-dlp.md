# yt-dlp

> Um fork do youtube-dl com funcionalidades e correções adicionais.
> Descarrega vídeos do YouTube e de outros websites.
> Mais informações: <https://github.com/yt-dlp/yt-dlp>.

- Descarrega um vídeo ou playlist (com as opções predefinidas):

`yt-dlp "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Descarrega um vídeo num formato específico, neste caso o melhor vídeo mp4 disponível (a predefinição é "bv\*+ba/b"):

`yt-dlp --format "{{bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]}}" "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Extrai áudio de vídeos (requer o `ffmpeg` ou o `ffprobe`):

`yt-dlp --extract-audio "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Especifica o formato de áudio extraído (a predefinição é "best"):

`yt-dlp --extract-audio --audio-format {{mp3}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Especifica a qualidade do áudio extraído, entre 0 (melhor) e 10 (pior), sendo 5 a predefinição:

`yt-dlp --extract-audio --audio-format {{mp3}} --audio-quality {{0}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Descarrega todas as playlists de um canal ou utilizador do YouTube, mantendo cada playlist num diretório separado:

`yt-dlp -o "{{%(uploader)s/%(playlist)s/%(indice_playlist)s - %(titulo)s.%(ext)s}}" "{{https://www.youtube.com/user/TheLinuxFoundation/playlists}}"`

- Descarrega um curso do Udemy, mantendo cada capítulo num diretório em separado, dentro do diretório "MyVideos" na home do utilizador:

`yt-dlp -u {{usuario}} -p {{palavra_passe}} -P "{{~/MyVideos}}" -o "{{%(playlist)s/%(numero_capitulo)s - %(capitulo)s/%(titulo)s.%(ext)s}}" "{{https://www.udemy.com/java-tutorial}}"`

- Descarrega temporadas completas de séries, mantendo cada série e cada temporada num diretório separado, em C:\MyVideos:

`yt-dlp -P "{{C:/MyVideos}}" -o "{{%(serie)s/%(numero_temporada)s - %(temporada)s/%(numero_episodio)s - %(episodio)s.%(ext)s}}" "{{https://videomore.ru/kino_v_detalayah/5_sezon/367617}}"`
