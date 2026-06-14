# youtube-dl

> Ներբեռնեք տեսանյութեր YouTube-ից և այլ կայքերից:.
> Տես նաև՝ `yt-dlp`, `ytfzf`, `you-get`:.
> Լրացուցիչ տեղեկություններ. <https://rg3.github.io/youtube-dl/>:.

- Ներբեռնեք տեսանյութ կամ երգացանկ.:

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Թվարկեք բոլոր ձևաչափերը, որոնցում հասանելի է տեսանյութը կամ երգացանկը.:

`youtube-dl {{[-F|--list-formats]}} '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Ներբեռնեք տեսանյութ կամ երգացանկ հատուկ որակով.:

`youtube-dl {{[-f|--format]}} "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Ներբեռնեք աուդիոն տեսանյութից և փոխարկեք այն MP3-ի.:

`youtube-dl {{[-x|--extract-audio]}} --audio-format {{mp3}} '{{url}}'`

- Ներբեռնեք լավագույն որակի աուդիո և վիդեո և միացրեք դրանք.:

`youtube-dl {{[-f|--format]}} bestvideo+bestaudio '{{url}}'`

- Ներբեռնեք տեսանյութ(ներ) որպես MP4 ֆայլեր՝ հատուկ ֆայլերի անուններով.:

`youtube-dl {{[-f|--format]}} {{mp4}} {{[-o|--output]}} "{{%(playlist_index)s-%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s}}" '{{url}}'`

- Ներբեռնեք որոշակի լեզվի ենթագրերը տեսանյութի հետ միասին.:

`youtube-dl --sub-lang {{en}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Ներբեռնեք երգացանկ և հանեք MP3-ները դրանից.:

`youtube-dl {{[-f|--format]}} "bestaudio" {{[-c|--continue]}} {{[-w|--no-overwrites]}} {{[-i|--ignore-errors]}} {{[-x|--extract-audio]}} --audio-format mp3 {{[-o|--output]}} "%(title)s.%(ext)s" '{{url_to_playlist}}'`
