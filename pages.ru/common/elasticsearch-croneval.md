# elasticsearch-croneval

> Проверять и вычислять выражения `cron`. Эта команда помогает убедиться, что выражения `cron` корректны для использования в Elasticsearch и дают ожидаемые результаты.
> Больше информации: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/elasticsearch-croneval>.

- Вычислить выражение `cron` и показать следующие 10 моментов срабатывания (поведение по умолчанию):

`elasticsearch-croneval "{{выражение_cron}}"`

- Вычислить выражение `cron` и показать конкретное количество будущих моментов срабатывания:

`elasticsearch-croneval "{{выражение_cron}}" {{[-c|--count]}} {{число}}`

- Показать подробную информацию (включая трассировку стека) для некорректного выражения `cron`:

`elasticsearch-croneval "{{некорректное_выражение_cron}}" {{[-d|--detail]}}`

- Показать минимальный вывод (тихий режим):

`elasticsearch-croneval "{{выражение_cron}}" {{[-s|--silent]}}`

- Показать подробный вывод:

`elasticsearch-croneval "{{выражение_cron}}" {{[-v|--verbose]}}`
