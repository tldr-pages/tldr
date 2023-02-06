# youtube-dl

> Videók letöltése a YouTube-ról és más weboldalakról. További információ: <http://rg3.github.io/youtube-dl/>.

- Videó vagy lejátszási lista letöltése:

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Az összes formátum felsorolása, amelyben egy videó vagy lejátszási lista elérhető:

`youtube-dl --list-formats '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Egy videó vagy lejátszási lista letöltése egy adott minőségben:

`youtube-dl --format "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Letöltheti a hangot egy videóból, és MP3-ba konvertálhatja:

`youtube-dl -x --audio-format {{mp3}} '{{url}}'`

- A legjobb minőségű hang és videó letöltése és egyesítése:

`youtube-dl -f bestvideo+bestaudio '{{url}}'`

- Videó(k) letöltése MP4 fájlként, egyéni fájlnevekkel:

`youtube-dl --format {{mp4}} -o "{{%(playlist_index)s-%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s}}" '{{url}}'`

- Egy adott nyelv feliratainak letöltése a videóval együtt:

`youtube-dl --sub-lang {{en}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Lejátszási lista letöltése és MP3-kivonás belőle:

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" {{url_to_playlist}}`
