# trackfetch

> Songs aus einer Textdatei als getaggte MP3-, M4A- oder Opus-Dateien herunterladen, mit Metadaten von Spotify und Audio von YouTube.
> Benötigt `yt-dlp`, `ffmpeg` sowie die Spotify-Client-ID und das Client-Secret (Konfigurationsdatei oder `SPOTIFY_CLIENT_ID` und `SPOTIFY_CLIENT_SECRET`).
> Weitere Informationen: <https://github.com/ByteMe6/trackfetch#usage>.

- Alle Songs aus einer Datei mit einer Zeile `Künstler - Titel` pro Song in das aktuelle Verzeichnis herunterladen:

`trackfetch {{path/to/songs.txt}}`

- Songs in ein bestimmtes Verzeichnis herunterladen:

`trackfetch {{path/to/songs.txt}} {{[-o|--output]}} {{path/to/directory}}`

- Das Original-Audio von YouTube behalten, statt es in MP3 umzuwandeln:

`trackfetch {{path/to/songs.txt}} {{[-f|--format]}} {{opus|m4a}}`

- Ein paar Titel ohne Textdatei herunterladen:

`trackfetch {{"Artist - Title"}} {{"Another Artist - Another Title"}}`

- Dateien nur nach dem Titel des Songs benennen, statt `Künstler - Titel`:

`trackfetch {{path/to/songs.txt}} --title-only`

- Eine Konfigurationsdatei für die Standardwerte verwenden:

`trackfetch {{path/to/songs.txt}} {{[--config]}} {{path/to/config.ini}}`

- Ein paar Sekunden zwischen den Songs warten, um keine Anfragelimits zu überschreiten:

`trackfetch {{path/to/songs.txt}} --delay {{3}}`

- Die Songs erneut versuchen, die beim vorherigen Lauf fehlgeschlagen sind:

`cut {{[-d|--delimiter]}} '|' {{[-f|--fields]}} 1 {{path/to/directory}}/failed.txt > {{path/to/retry.txt}} && trackfetch {{path/to/retry.txt}} {{[-o|--output]}} {{path/to/directory}}`
