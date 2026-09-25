# youtube-dl

> Download video's van YouTube en andere websites.
> Zie ook: `yt-dlp`, `ytfzf`, `you-get`.
> Meer informatie: <https://rg3.github.io/youtube-dl/>.

- Download een video of afspeellijst:

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Toon alle formaten waarin een video of afspeellijst beschikbaar is:

`youtube-dl {{[-F|--list-formats]}} '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Download een video of afspeellijst met een specifieke kwaliteit:

`youtube-dl {{[-f|--format]}} "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Download de audio van een video en converteer het naar MP3:

`youtube-dl {{[-x|--extract-audio]}} --audio-format {{mp3}} '{{url}}'`

- Download de best mogelijke audio en video en voeg ze samen:

`youtube-dl {{[-f|--format]}} bestvideo+bestaudio '{{url}}'`

- Download video('s) als MP4-bestanden met aangepaste bestandsnamen:

`youtube-dl {{[-f|--format]}} {{mp4}} {{[-o|--output]}} "{{%(playlist_index)s-%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s}}" '{{url}}'`

- Download de ondertiteling van een specifieke taal samen met de video:

`youtube-dl --sub-lang {{en}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Download een afspeellijst en extraheer er MP3's uit:

`youtube-dl {{[-f|--format]}} "bestaudio" {{[-c|--continue]}} {{[-w|--no-overwrites]}} {{[-i|--ignore-errors]}} {{[-x|--extract-audio]}} --audio-format mp3 {{[-o|--output]}} "%(title)s.%(ext)s" '{{url_to_playlist}}'`
