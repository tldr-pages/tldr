# weasyprint

> Перевод HTML в PDF или PNG.
> Больше информации: <https://doc.courtbouillon.org/weasyprint/stable/api_reference.html#command-line-api>.

- Перевести HTML файл в PDF:

`weasyprint {{путь/ко/входному.html}} {{путь/к/выходному.pdf}}`

- Перевести HTML файл в PNG, включая дополнительные пользовательские таблицы стилей:

`weasyprint {{путь/ко/входному.html}} {{путь/к/выходному.png}} --stylesheet {{путь/к/таблице_стилей.css}}`

- При переводе выводить дополнительную отладочную информацию:

`weasyprint {{путь/ко/входному.html}} {{путь/к/выходному.pdf}} --verbose`

- При выводе в PNG указать нестандартное разрешение:

`weasyprint {{путь/ко/входному.html}} {{путь/к/выходному.png}} --resolution {{300}}`

- Во входном HTML файле указать базовый URL для относительных URLs:

`weasyprint {{путь/ко/входному.html}} {{путь/к/выходному.png}} --base-url {{url_или_имя_файла}}`
