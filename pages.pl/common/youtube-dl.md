# youtube-dl

> Pobieraj wideo i audio z YouTube i podobnych portali
> Więcej informacji: <http://rg3.github.io/youtube-dl/>.

- Pobierz plik wideo lub wszystkie pliki z playlisty:

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Listuj wszystkie formaty dostępne dla filmu lub playlisty:

`youtube-dl --list-formats '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Pobierz wideo lub playlistę w wybranej jakości:

`youtube-dl --format "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Pobierz audio z wideo w formacie mp3:

`youtube-dl -x --audio-format {{mp3}} '{{url}}'`

- Pobierz wideo ze ścieżką audio złączone w jendym pliku w najlepszej dostępnej jakości:

`youtube-dl -f bestvideo+bestaudio '{{url}}'`

- Pobierz wideo jako pliki MP4 i nazwij wedle schematu:

`youtube-dl --format {{mp4}} -o "{{%(title)s by %(uploader)s on %(upload_date)s in %(playlist)s.%(ext)s}}" '{{url}}'`

- Pobierz plik razem z napisami:

`youtube-dl --sub-lang {{en}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Pobierz ścieżkę dźwiękową ze wszystkich filmów z playlisty:

`youtube-dl -i --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" '{{adres_url_playlisty}}'`
