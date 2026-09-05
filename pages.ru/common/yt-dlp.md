# yt-dlp

> Форк youtube-dl с дополнительными возможностями и исправлениями.
> Загружает видео с YouTube и других сайтов.
> Смотрите также: `ytfzf`.
> Больше информации: <https://github.com/yt-dlp/yt-dlp#usage-and-options>.

- Скачать видео или плейлист (с параметрами по умолчанию):

`yt-dlp "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Вывести список доступных для скачивания форматов видео:

`yt-dlp {{[-F|--list-formats]}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Скачать видео или плейлист в лучшем доступном формате MP4 (по умолчанию "bv\*+ba/b"):

`yt-dlp {{[-f|--format]}} "{{bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4]}}" "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Извлечь аудио из видео (требуется ffmpeg или ffprobe):

`yt-dlp {{[-x|--extract-audio]}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Указать формат и качество извлекаемого аудио (от 0 (лучшее) до 10 (худшее), по умолчанию 5):

`yt-dlp {{[-x|--extract-audio]}} --audio-format {{mp3}} --audio-quality {{0}} "{{https://www.youtube.com/watch?v=oHg5SJYRHA0}}"`

- Скачать только второй, с четвёртого по шестой и последний элементы плейлиста (нумерация начинается с 1, а не с 0):

`yt-dlp {{[-I|--playlist-items]}} 2,4:6,-1 "{{https://youtube.com/playlist?list=PLbzoR-pLrL6pTJfLQ3UwtB-3V4fimdqnA}}"`

- Скачать все плейлисты канала/пользователя YouTube, сохраняя каждый плейлист в отдельный каталог:

`yt-dlp {{[-o|--output]}} "{{%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s}}" "{{https://www.youtube.com/user/TheLinuxFoundation/playlists}}"`

- Скачать курс Udemy, сохраняя каждую главу в отдельный каталог:

`yt-dlp {{[-u|--username]}} {{пользователь}} {{[-p|--password]}} {{пароль}} {{[-P|--paths]}} "{{путь/к/каталогу}}" {{[-o|--output]}} "{{%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s}}" "{{https://www.udemy.com/java-tutorial}}"`
