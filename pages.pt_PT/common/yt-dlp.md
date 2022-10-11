# yt-dlp

> Um fork do youtube-dl com funcionalidades e correções adicionais.
> Descarrega vídeos do YouTube e de outros websites.
> Mais informações: <https://github.com/yt-dlp/yt-dlp>.

- Descarregar um vídeo ou playlist (com as predefinições do comando abaixo):

`yt-dlp "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Descarregar um vídeo com um formato definido. Neste caso, fundindo o melhor formato de vídeo com o melhor formato de áudio (Predefinição):

`yt-dlp --format "{{bv*+ba/b}}" "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Extrair áudio de vídeos (necessário ffmpeg ou ffprobe):

`yt-dlp --extract-audio "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Especificar o formato de áudio extraído (best(predefinição), acc, flac, mp3, m4a, opus, vorbis, wav, alac):

`yt-dlp --extract-audio --audio-format {{mp3}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Especificar a qualidade do áudio extraído (entre 0 (melhor) e 10 (pior), predefinição = 5):

`yt-dlp --extract-audio --audio-format {{mp3}} --audio-quality {{0}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Descarregar todas as playlists de um canal/usuário de YouTube, mantendo cada playlist num diretório em separado:

`yt-dlp -o "{{%(uploader)s/%(playlist)s/%(indice_playlist)s - %(titulo)s.%(ext)s}}" "{{https://www.youtube.com/user/TheLinuxFoundation/playlists}}"`

- Descarregar um curso de Udemy, mantendo cada capítulo num diretório em separado, dentro do diretório MyVideos na sua home:

`yt-dlp -u {{usuario}} -p {{palavra_passe}} -P "{{~/MyVideos}}" -o "{{%(playlist)s/%(numero_capitulo)s - %(capitulo)s/%(titulo)s.%(ext)s}}" "{{https://www.udemy.com/java-tutorial}}"`

- Descarregar temporadas completas de séries, mantendo cada série e cada temporada num diretório em separado, em C:\MyVideos:

`yt-dlp -P "{{C:/MyVideos}}" -o "{{%(serie)s/%(numero_temporada)s - %(temporada)s/%(numero_episodio)s - %(episodio)s.%(ext)s}}" "{{https://videomore.ru/kino_v_detalayah/5_sezon/367617}}"`
