# curl

> Передавать данные с сервера или на сервер.
> Поддерживает большинство протоколов, включая HTTP, HTTPS, FTP, SCP и другие.
> Смотрите также: `wcurl`, `wget`.
> Больше информации: <https://curl.se/docs/manpage.html>.

- Выполнить HTTP GET-запрос и вывести содержимое в `stdout`:

`curl {{https://example.com}}`

- Выполнить HTTP GET-запрос, следовать перенаправлениям `3xx` и вывести заголовки ответа и содержимое в `stdout`:

`curl {{[-L|--location]}} {{[-D|--dump-header]}} - {{https://example.com}}`

- Скачать файл, сохранив его под именем, указанным в URL:

`curl {{[-O|--remote-name]}} {{https://example.com/filename.zip}}`

- Отправить данные формы (POST-запрос типа `application/x-www-form-urlencoded`). Используйте `--data @file_name` или `--data @'-'` для чтения из `stdin`:

`curl {{[-X|--request]}} POST {{[-d|--data]}} '{{name=bob}}' {{http://example.com/form}}`

- Отправить запрос с дополнительным заголовком, пользовательским HTTP-методом через прокси (например, BurpSuite), игнорируя самоподписанные сертификаты:

`curl {{[-k|--insecure]}} {{[-x|--proxy]}} {{http://127.0.0.1:8080}} {{[-H|--header]}} '{{Authorization: Bearer token}}' {{[-X|--request]}} {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- Отправить данные в формате JSON, указав соответствующий заголовок Content-Type:

`curl {{[-d|--data]}} '{{{"name":"bob"}}}' {{[-H|--header]}} '{{Content-Type: application/json}}' {{http://example.com/users/1234}}`

- Передать клиентский сертификат и закрытый ключ для запроса, пропуская проверку сертификата:

`curl {{[-E|--cert]}} {{client.pem}} --key {{key.pem}} {{[-k|--insecure]}} {{https://example.com}}`

- Привязать имя хоста к определённому IP-адресу с подробным выводом (аналог редактирования `/etc/hosts`):

`curl {{[-v|--verbose]}} --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
