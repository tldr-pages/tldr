# trackfetch

> Скачивать песни, перечисленные в текстовом файле, как файлы MP3, M4A или Opus с тегами, используя метаданные Spotify и звук из YouTube.
> Требуются `yt-dlp`, `ffmpeg`, а также ID и секрет клиента Spotify (файл конфигурации или `SPOTIFY_CLIENT_ID` и `SPOTIFY_CLIENT_SECRET`).
> Больше информации: <https://github.com/ByteMe6/trackfetch#usage>.

- Скачать все песни из файла, где на каждой строке `Исполнитель - Название`, в текущую директорию:

`trackfetch {{path/to/songs.txt}}`

- Скачать песни в конкретную директорию:

`trackfetch {{path/to/songs.txt}} {{[-o|--output]}} {{path/to/directory}}`

- Сохранить оригинальный звук из YouTube вместо конвертации в MP3:

`trackfetch {{path/to/songs.txt}} {{[-f|--format]}} {{opus|m4a}}`

- Скачать несколько треков без текстового файла:

`trackfetch {{"Artist - Title"}} {{"Another Artist - Another Title"}}`

- Назвать файлы только названием песни вместо `Исполнитель - Название`:

`trackfetch {{path/to/songs.txt}} --title-only`

- Использовать файл конфигурации со значениями по умолчанию:

`trackfetch {{path/to/songs.txt}} {{[--config]}} {{path/to/config.ini}}`

- Подождать несколько секунд между песнями, чтобы избежать ограничения частоты запросов:

`trackfetch {{path/to/songs.txt}} --delay {{3}}`

- Повторить попытку для песен, которые не удались при предыдущем запуске:

`cut {{[-d|--delimiter]}} '|' {{[-f|--fields]}} 1 {{path/to/directory}}/failed.txt > {{path/to/retry.txt}} && trackfetch {{path/to/retry.txt}} {{[-o|--output]}} {{path/to/directory}}`
