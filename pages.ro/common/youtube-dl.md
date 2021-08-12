# youtube-dl

> Descărcați videoclipuri de pe YouTube și alte site-uri web.
> Mai multe informaţii: <http://rg3.github.io/youtube-dl/>

- Descărcați un videoclip sau o listă de redare:

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Listează toate formatele în care este disponibil un videoclip sau o listă de redare:

`youtube-dl --list-formats '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Descărcați un videoclip sau o listă de redare la o anumită calitate:

`youtube-dl --format "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Descărcați sunetul dintr-un videoclip și convertiți-l într-un MP3:

`youtube-dl -x --audio-format {{mp3}} '{{url}}'`

- Descărcați cele mai bune audio și video de calitate și îmbinați-le:

`youtube-dl -f bestvideo+bestaudio '{{url}}'`

- Descărcați video (e) ca fișiere MP4 cu nume de fișiere personalizate:

`youtube-dl --format {{mp4}} -o "{{%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s}}" '{{url}}'`

- Descărcați subtitrările unei anumite limbi împreună cu videoclipul:

`youtube-dl --sub-lang {{en}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Descărcați o listă de redare și extrageți mp3 din ea:

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" {{url_to_playlist}}`
