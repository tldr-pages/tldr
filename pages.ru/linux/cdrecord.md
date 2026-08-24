# cdrecord

> Записывать данные на CD или DVD.
> Некоторые вызовы cdrecord могут привести к деструктивным действиям, таким как стирание всех данных на диске.
> Больше информации: <https://manned.org/cdrecord>.

- Показать оптические приводы, доступные для `cdrecord`:

`cdrecord --devices`

- Записать ("burn") диск только с аудио:

`cdrecord dev={{/dev/optical_drive}} -audio {{track*.cdaudio}}`

- Записать файл на диск с извлечением диска по завершении (некоторые рекордеры требуют этого):

`cdrecord -eject dev={{/dev/optical_drive}} -data {{file.iso}}`

- Записать файл на диск в оптическом приводе с возможностью записи на несколько дисков подряд:

`cdrecord -tao dev={{/dev/optical_drive}} -data {{file.iso}}`
