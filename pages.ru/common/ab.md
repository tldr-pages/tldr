# ab

> Утилита бенчмаркинга Apache. Самая простая утилита для проведения нагрузочного тестирования.
> Больше информации: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Запустить 100 запросов HTTP GET по заданному URL:

`ab -n 100 {{url}}`

- Запустить 100 запросов HTTP GET, обрабатывая до 10 одновременно, по заданному URL:

`ab -n 100 -c 10 {{url}}`

- Запустить 100 запросов HTTP POST по заданному URL, используя в качестве полезной нагрузки JSON из файла:

`ab -n 100 -T {{application/json}} -p {{путь/до/файла.json}} {{url}}`

- Использовать постоянное соединение (keep-alive):

`ab -k {{url}}`

- Задать максимальное число секунд, которое можно затратить на бенчмаркинг:

`ab -t {{60}} {{url}}`
