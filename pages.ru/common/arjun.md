# arjun

> Искать HTTP-параметры веб-приложений.
> Больше информации: <https://github.com/s0md3v/Arjun/wiki/Usage>.

- Просканировать URL-адрес на наличие GET-параметров:

`arjun -u {{https://example.com/page.php}}`

- Просканировать, используя метод POST:

`arjun -u {{https://example.com/api}} -m POST`

- Сохранить найденные параметры в JSON-файл:

`arjun -u {{https://example.com}} -o {{путь/к/выходному_файлу.json}}`

- Использовать пользовательский словарь (wordlist):

`arjun -u {{https://example.com}} -w {{путь/к/словарю.txt}}`

- Увеличить задержку между запросами на указанное количество секунд, чтобы избежать ограничения частоты запросов (rate limiting):

`arjun -u {{https://example.com}} -d {{2}}`
