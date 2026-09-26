# yt-dlp

> Een youtube-dl fork met extra functies en fixes.
> Download video's van YouTube en andere websites.
> Zie ook: `ytfzf`.
> Meer informatie: <https://github.com/yt-dlp/yt-dlp#usage-and-options>.

- Download een video of afspeellijst (met de standaardopties van onderstaand commando):

`yt-dlp "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Toon de beschikbare downloadbare formaten voor een video:

`yt-dlp {{[-F|--list-formats]}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Download een video of afspeellijst met de best beschikbare MP4-video (standaard is "bv\*+ba/b"):

`yt-dlp {{[-f|--format]}} "{{bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]}}" "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Extraheer audio uit een video (vereist ffmpeg of ffprobe):

`yt-dlp {{[-x|--extract-audio]}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Specificeer het audioformaat en de audiokwaliteit van de geëxtraheerde audio (tussen 0 (beste) en 10 (slechtste), standaard = 5):

`yt-dlp {{[-x|--extract-audio]}} --audio-format {{mp3}} --audio-quality {{0}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Download alleen het tweede, vierde, vijfde, zesde en laatste item in een afspeellijst (het eerste item is 1, niet 0):

`yt-dlp {{[-I|--playlist-items]}} 2,4:6,-1 "{{https://youtube.com/playlist?list=PLbzoR-pLrL6pTJfLQ3UwtB-3V4fimdqnA}}"`

- Download alle afspeellijsten van een YouTube-kanaal/gebruiker, waarbij elke afspeellijst in een aparte map wordt bewaard:

`yt-dlp {{[-o|--output]}} "{{%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s}}" "{{https://www.youtube.com/user/TheLinuxFoundation/playlists}}"`

- Download een Udemy-cursus, waarbij elk hoofdstuk in een aparte map wordt bewaard:

`yt-dlp {{[-u|--username]}} {{gebruiker}} {{[-p|--password]}} {{wachtwoord}} {{[-P|--paths]}} "{{pad/naar/map}}" {{[-o|--output]}} "{{%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s}}" "{{https://www.udemy.com/java-tutorial}}"`
