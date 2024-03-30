# gcloud sql export sql

> Export data from a Cloud SQL instance to an SQL file in Google Cloud Storage.
> Useful for creating backups or migrating data. See also: `gcloud`.
> More information: <https://cloud.google.com/sdk/gcloud/reference/sql/export/sql>.

- Export data from a specific Cloud SQL instance to a Google Cloud Storage bucket as an SQL dump file:

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}}`

- Export data asynchronously, returning immediately without waiting for the operation to complete:

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --async`

- Export data from specific databases within the Cloud SQL instance:

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --database={{database1,database2,...}}`

- Export specific tables from a specified database within the Cloud SQL instance:

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --database={{database}} --table={{table1,table2,...}}`

- Export data while offloading the operation to a temporary instance to reduce strain on the source instance:

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}} --offload`

- Export data and compress the output with `gzip`:

`gcloud sql export sql {{instance}} gs://{{bucket_name}}/{{file_name}}.gz`
