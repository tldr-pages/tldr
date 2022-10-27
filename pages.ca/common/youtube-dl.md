# youtube-dl

> Descarrega videos de YouTube i altres pàgines web.
> Més informació: <http://rg3.github.io/youtube-dl/>.

- Descarrega un vídeo o playlist:

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Llista tots els formats en el que es troba disponible un vídeo o playlist:

`youtube-dl --list-formats '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Descarrega un vídeo o playlist en una qualitat específica:

`youtube-dl --format "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Descarrega l'àudio d'un vídeo i converteix-lo a MP3:

`youtube-dl -x --audio-format {{mp3}} '{{url}}'`

- Descarrega l'àudio i el vídeo de major qualitat i fusiona'ls:

`youtube-dl -f bestvideo+bestaudio '{{url}}'`

- Descarrega vídeo(s) com a fitxers MP4 amb un nom específic:

`youtube-dl --format {{mp4}} -o "{{%(playlist_index)s-%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s}}" '{{url}}'`

- Descarrega els subtítols d'un llenguatge en concret amb el vídeo:

`youtube-dl --sub-lang {{en}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Descarrega una playlist i extreu-ne els MP3s:

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" {{url_to_playlist}}`
