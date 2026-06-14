# բք

> Python-ի վրա հիմնված գործիք BigQuery-ի համար՝ Google Cloud-ի ամբողջությամբ կառավարվող և ամբողջովին առանց սերվերի ձեռնարկության տվյալների պահեստ:.
> Լրացուցիչ տեղեկություններ. <https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference>:.

- Գործարկեք հարցումը BigQuery աղյուսակի հետ՝ օգտագործելով ստանդարտ SQL, ավելացրեք `--dry_run` դրոշը՝ հարցման կողմից կարդացվող բայթերի քանակը գնահատելու համար.:

`bq query --nouse_legacy_sql 'SELECT COUNT(*) FROM {{DATASET_NAME}}.{{TABLE_NAME}}'`

- Գործարկել պարամետրացված հարցում.:

`bq query --use_legacy_sql=false --parameter='ts_value:TIMESTAMP:2016-12-07 08:00:00' 'SELECT TIMESTAMP_ADD(@ts_value, INTERVAL 1 HOUR)'`

- Ստեղծեք նոր տվյալների բազա կամ աղյուսակ ԱՄՆ-ի գտնվելու վայրում.:

`bq mk --location=US {{dataset_name}}.{{table_name}}`

- Թվարկեք բոլոր տվյալների հավաքածուները նախագծի մեջ.:

`bq ls --filter labels.{{key}}:{{value}} --max_results {{integer}} --format=prettyjson --project_id {{project_id}}`

- Խմբաքանակի բեռնման տվյալները որոշակի ֆայլից այնպիսի ձևաչափերով, ինչպիսիք են CSV, JSON, Parquet և Avro, աղյուսակում.:

`bq load --location {{location}} --source_format {{CSV|JSON|PARQUET|AVRO}} {{dataset}}.{{table}} {{path/to/source}}`

- Պատճենեք մի աղյուսակը մյուսին.:

`bq cp {{dataset}}.{{OLD_TABLE}} {{dataset}}.{{new_table}}`

- Ցուցադրել օգնությունը.:

`bq help`
