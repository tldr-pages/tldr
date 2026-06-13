# youtube-dl

> Unduh video dari YouTube dan situs web lain.
> Lihat juga: `yt-dlp`, `ytfzf`, `you-get`.
> Informasi lebih lanjut: <https://rg3.github.io/youtube-dl/>.

- Unduh suatu video atau daftar putar:

`youtube-dl '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Tampilkan daftar format yang tersedia untuk video atau daftar putar:

`youtube-dl {{[-F|--list-formats]}} '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Unduh video atau daftar putar dengan kualitas tertentu:

`youtube-dl {{[-f|--format]}} "{{best[height<=480]}}" '{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}'`

- Unduh audio dari suatu video dan ubah menjadi berkas MP3:

`youtube-dl {{[-x|--extract-audio]}} --audio-format {{mp3}} '{{url}}'`

- Unduh gabungan video dan audio dengan kualitas terbaik:

`youtube-dl {{[-f|--format]}} bestvideo+bestaudio '{{url}}'`

- Unduh satu atau beberapa video sebagai berkas MP4 dengan nama tertentu:

`youtube-dl {{[-f|--format]}} {{mp4}} {{[-o|--output]}} "{{%(playlist_index)s-%(title)s oleh %(uploader)s pada %(upload_date)s di dalam %(playlist)s.%(ext)s}}" '{{url}}'`

- Unduh video bersama dengan subtitle bahasa tertentu:

`youtube-dl --sub-lang {{en}} --write-sub '{{https://www.youtube.com/watch?v=Mwa0_nE9H7A}}'`

- Mengunduh daftar putar dan ekstrak MP3 darinya:

`youtube-dl {{[-f|--format]}} "bestaudio" {{[-c|--continue]}} {{[-w|--no-overwrites]}} {{[-i|--ignore-errors]}} {{[-x|--extract-audio]}} --audio-format mp3 {{[-o|--output]}} "%(title)s.%(ext)s" '{{url_to_playlist}}'`
