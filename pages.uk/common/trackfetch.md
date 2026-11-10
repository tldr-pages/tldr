# trackfetch

> Завантажувати пісні з текстового файлу як файли MP3, M4A або Opus із тегами, використовуючи метадані Spotify і звук із YouTube.
> Потрібні `yt-dlp`, `ffmpeg` та client ID і client secret від Spotify (файл конфігурації або `SPOTIFY_CLIENT_ID` і `SPOTIFY_CLIENT_SECRET`).
> Більше інформації: <https://github.com/ByteMe6/trackfetch#usage>.

- Завантажити всі пісні з файлу, де в кожному рядку `Виконавець - Назва`, у поточну директорію:

`trackfetch {{path/to/songs.txt}}`

- Завантажити пісні у конкретну директорію:

`trackfetch {{path/to/songs.txt}} {{[-o|--output]}} {{path/to/directory}}`

- Зберегти оригінальний звук із YouTube замість конвертації у MP3:

`trackfetch {{path/to/songs.txt}} {{[-f|--format]}} {{opus|m4a}}`

- Завантажити кілька треків без текстового файлу:

`trackfetch {{"Artist - Title"}} {{"Another Artist - Another Title"}}`

- Називати файли лише назвою пісні замість `Виконавець - Назва`:

`trackfetch {{path/to/songs.txt}} --title-only`

- Використати файл конфігурації зі значеннями за замовчуванням:

`trackfetch {{path/to/songs.txt}} {{[--config]}} {{path/to/config.ini}}`

- Чекати кілька секунд між піснями, щоб не впитися в ліміти запитів:

`trackfetch {{path/to/songs.txt}} --delay {{3}}`

- Повторити спробу для пісень, які не завантажилися минулого разу:

`cut {{[-d|--delimiter]}} '|' {{[-f|--fields]}} 1 {{path/to/directory}}/failed.txt > {{path/to/retry.txt}} && trackfetch {{path/to/retry.txt}} {{[-o|--output]}} {{path/to/directory}}`
