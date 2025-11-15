# aws

> Alat baris perintah (CLI) resmi untuk Amazon Web Services.
> Beberapa subperintah seperti `s3` mempunyai dokumentasi terpisah.
> Informasi lebih lanjut: <https://aws.amazon.com/cli>.

- Atur penggunaan AWS Command-line secara umum:

`aws configure wizard`

- Atur penggunaan AWS Command-line menggunakan SSO:

`aws configure sso`

- Dapatkan identitas pemanggil perintah (digunakan untuk menyelesaikan permasalahan yang berkaitan dengan hak akses):

`aws sts get-caller-identity`

- Tampilkan daftar sumber daya AWS dalam suatu wilayah (region) ke dalam format YAML:

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- Gunakan fitur auto prompt untuk membantu melakukan suatu perintah:

`aws iam create-user --cli-auto-prompt`

- Jalankan perintah wizard terhadap suatu sumber daya AWS:

`aws dynamodb wizard {{new_table}}`

- Buat suatu berkas JSON CLI Skeleton (berguna untuk mengatur infrastruktur sebagai perintah kode):

`aws dynamodb update-table --generate-cli-skeleton`

- Tampilkan bantuan terhadap suatu perintah:

`aws {{perintah}} help`
