# wcurl

> Простая обёртка над `curl` для удобной загрузки файлов.
> Смотрите также: `wget`, `curl`.
> Больше информации: <https://curl.se/wcurl/manual.html>.

- Скачать содержимое URL в файл, указанный в URL (в данном случае `index.html`):

`wcurl {{https://example.com/index.html}}`

- Скачать содержимое URL в файл с указанным именем:

`wcurl {{[-o|--output]}} {{путь/к/файлу}} {{https://example.com/index.html}}`

- Скачать содержимое URL с индикатором прогресса и использованием HTTP/2 по умолчанию:

`wcurl --curl-options "--progress-bar --http2" {{https://example.com/index.html}}`

- Возобновить прерванную загрузку:

`wcurl --curl-options "--clobber --continue-at -" {{https://example.com/index.html}}`
