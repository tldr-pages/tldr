# youtube-dl

> Scarica video da YouTube ed altri siti web.
> Maggiori informazioni: <http://rg3.github.io/youtube-dl/>.

- Scarica un video od una playlist:

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Elenca tutti i formati in cui un video od una playlist sono disponibili:

`youtube-dl --list-formats '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Scarica un video od una playlist con la qualità specificata:

`youtube-dl --format "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Scarica l'audio di un video e lo converte in file MP3:

`youtube-dl -x --audio-format {{mp3}} '{{url}}'`

- Scarica l'audio di migliore qualità e il video di migliore qualità e li unisce:

`youtube-dl -f bestvideo+bestaudio '{{url}}'`

- Scarica una playlist di video e li salva come file MP4 dai nomi personalizzati:

`youtube-dl --format {{mp4}} -o "{{%(title)s di %(uploader)s del %(upload_date)s in %(playlist)s.%(ext)s}}" '{{url}}'`

- Scarica, assieme al video, i sottotitoli in una lingua specificata:

`youtube-dl --sub-lang {{it}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Scarica una playlist, ne estrae l'audio e lo salva in formato mp3:

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" '{{url_della_playlist}}'`
