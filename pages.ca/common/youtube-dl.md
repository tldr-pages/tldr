# youtube-dl

> Descarrega videos de YouTube i altres pàgines web.
> Vegeu també: `yt-dlp`, `ytfzf`, `you-get`.
> Més informació: <https://rg3.github.io/youtube-dl/>.

- Descarrega un vídeo o playlist:

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Llista tots els formats en el que es troba disponible un vídeo o playlist:

`youtube-dl {{[-F|--list-formats]}} '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Descarrega un vídeo o playlist en una qualitat específica:

`youtube-dl {{[-f|--format]}} "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Descarrega l'àudio d'un vídeo i converteix-lo a MP3:

`youtube-dl {{[-x|--extract-audio]}} --audio-format {{mp3}} '{{url}}'`

- Descarrega l'àudio i el vídeo de major qualitat i fusiona'ls:

`youtube-dl {{[-f|--format]}} bestvideo+bestaudio '{{url}}'`

- Descarrega vídeo(s) com a fitxers MP4 amb un nom específic:

`youtube-dl {{[-f|--format]}} {{mp4}} {{[-o|--output]}} "{{%(playlist_index)s-%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s}}" '{{url}}'`

- Descarrega els subtítols d'un llenguatge en concret amb el vídeo:

`youtube-dl --sub-lang {{en}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Descarrega una playlist i extreu-ne els MP3s:

`youtube-dl {{[-f|--format]}} "bestaudio" {{[-c|--continue]}} {{[-w|--no-overwrites]}} {{[-i|--ignore-errors]}} {{[-x|--extract-audio]}} --audio-format mp3 {{[-o|--output]}} "%(title)s.%(ext)s" '{{url_to_playlist}}'`
