# youtube-dl

> Unduh video dari YouTube dan situs web lain.
> Informasi lebih lanjut: <http://rg3.github.io/youtube-dl/>.

- Mengunduh sebuah video atau daftar putar:

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Tampilkan daftar format yang tersedia untuk video atau daftar putar:

`youtube-dl --list-formats '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Mengunduh video atau daftar putar dengan kualitas tertentu:

`youtube-dl --format "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Mengunduh audio dari video dan ubah menjadi MP3:

`youtube-dl -x --audio-format {{mp3}} '{{url}}'`

- Mengunduh video dan audio dengan kualitas terbaik lalu gabungkan:

`youtube-dl -f bestvideo+bestaudio '{{url}}'`

- Mengunduh satu atau beberapa video sebagai file MP4 dengan nama tertentu:

`youtube-dl --format {{mp4}} -o "{{%(playlist_index)s-%(title)s oleh %(uploader)s pada %(upload_date)s di dalam %(playlist)s.%(ext)s}}" '{{url}}'`

- Mengunduh video bersama dengan subtitle bahasa tertentu:

`youtube-dl --sub-lang {{en}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Mengunduh daftar putar dan ekstrak MP3 darinya:

`youtube-dl -f "bestaudio" --continue --no-overwrites --ignore-errors --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" {{url_to_playlist}}`
