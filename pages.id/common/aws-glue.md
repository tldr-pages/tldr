# aws glue

> Program baris perintah untuk AWS Glue.
> Tentukan endpoint publik untuk layanan AWS Glue.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/glue/>.

- Tampilkan daftar pekerjaan:

`aws glue list-jobs`

- Jalankan suatu pekerjaan:

`aws glue start-job-run --job-name {{nama_pekerjaan}}`

- Jalankan suatu alur kerja (workflow):

`aws glue start-workflow-run --name {{nama_alur_kerja}}`

- Tampilkan daftar pemicu pekerjaan:

`aws glue list-triggers`

- Jalankan suatu pemicu pekerjaan:

`aws glue start-trigger --name {{nama_pemicu}}`

- Buat suatu endpoint versi pengembangan:

`aws glue create-dev-endpoint --endpoint-name {{nama}} --role-arn {{role_arn_yang_digunakan_dalam_endpoint}}`
