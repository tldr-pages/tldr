# bq

> Alat pemrosesan data berbasis Python untuk BigQuery, layanan pergudangan data Google Cloud yang sepenuhnya terkelola dan bersifat serverless.
> Informasi lebih lanjut: <https://cloud.google.com/bigquery/docs/reference/bq-cli-reference>.

- Jalankan suatu perintah kueri terhadap suatu tabel BigQuery dalam format SQL dasar, tambahkan opsi `--dry_run` untuk menaksir jumlah bita yang akan dibaca pada proses eksekusi:

`bq query --nouse_legacy_sql 'SELECT COUNT(*) FROM {{NAMA_DATASET}}.{{NAMA_TABEL}}'`

- Jalankan suatu perintah kueri dengan kumpulan parameter:

`bq query --use_legacy_sql=false --parameter='ts_value:TIMESTAMP:2016-12-07 08:00:00' 'SELECT TIMESTAMP_ADD(@ts_value, INTERVAL 1 HOUR)'`

- Buat suatu dataset atau tabel pada wilayah layanan Amerika Serikat (US):

`bq mk --location=US {{nama_dataset}}.{{nama_tabel}}`

- Tampilkan seluruh dataset pada suatu proyek:

`bq ls --filter labels.{{key}}:{{value}} --max_results {{integer}} --format=prettyjson --project_id {{id_proyek}}`

- Lakukan proses pemuatan data secara batch dari berkas tertentu dalam format seperti CSV, JSON, Parquet, dan Avro ke dalam suatu tabel:

`bq load --location {{lokasi}} --source_format {{CSV|JSON|PARQUET|AVRO}} {{dataset}}.{{table}} {{jalan_menuju_sumber}}`

- Salin suatu tabel menuju tabel lainnya:

`bq cp {{dataset}}.{{TABEL_LAMA}} {{dataset}}.{{tabel_baru}}`

- Tampilkan bantuan:

`bq help`
