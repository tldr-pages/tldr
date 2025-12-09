# elasticsearch-croneval

> Validates and evaluates a `cron` expression. This command helps verify that `cron` expressions are valid for use with Elasticsearch and produce the expected results.
> More information: <https://www.elastic.co/guide/en/elasticsearch/reference/current/elasticsearch-croneval.html>.

- Evaluate a `cron` expression and display the next 10 trigger times (default behavior):

`elasticsearch-croneval "{{cron_expression}}"`

- Evaluate a `cron` expression and display a specific number of future trigger times:

`elasticsearch-croneval "{{cron_expression}}" {{[-c|--count]}} {{integer}}`

- Display detailed information (including stack trace) for an invalid `cron` expression:

`elasticsearch-croneval "{{invalid_cron_expression}}" {{[-d|--detail]}}`

- Display minimal output (silent mode):

`elasticsearch-croneval "{{cron_expression}}" {{[-s|--silent]}}`

- Display verbose output:

`elasticsearch-croneval "{{cron_expression}}" {{[-v|--verbose]}}`
