# bq

> A bq parancssori eszköz egy Python-alapú parancssori eszköz a BigQuery-hez. További információ: <https://cloud.google.com/bigquery/docs/reference/bq-cli-reference>.

- Futtasson lekérdezést egy BigQuery-táblán a szokásos SQL használatával, adjon hozzá `--dry_run` flaget a lekérdezés által olvasott bájtok számának becsléséhez:

`bq query --nouse_legacy_sql 'SELECT COUNT(*) FROM {{DATASET_NAME}}.{{TABLE_NAME}}'`

- Paraméteres lekérdezés futtatása:

`bq query --use_legacy_sql=false --parameter='ts_value:TIMESTAMP:2016-12-07 08:00:00' 'SELECT TIMESTAMP_ADD(@ts_value, INTERVAL 1 HOUR)'`

- Új adatállomány vagy tábla létrehozása az amerikai helyen:

`bq mk --location=US {{dataset_name}}.{{table_name}}`

- A projektben lévő összes adatkészlet listázása:

`bq ls --filter labels.{{key}}:{{value}} --max_results {{integer}} --format=prettyjson --project_id {{project_id}}`

- Adatok kötegelt betöltése egy adott fájlból, például CSV, JSON, Parquet és Avro formátumban egy táblázatba:

`bq load --location={{location}} --source_format={{CSV|JSON|PARQUET|AVRO}} {{dataset}}.{{table}} {{path_to_source}}`

- Egy táblázat másolása egy másikba:

`bq cp {{dataset}}.{{OLD_TABLE}} {{dataset}}.{{new_table}}`

- Súgó nyomtatása:

`bq help`
