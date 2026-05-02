# aws s3 cp

> Salin kumpulan berkas lokal atau objek S3 menuju lokasi lainnya baik dalam penyimpanan lokal maupun S3.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html>.

- Salin suatu berkas dari penyimpanan lokal menuju suatu ember (bucket):

`aws s3 cp {{jalan/menuju/berkas}} s3://{{nama_ember}}/{{jalan/menuju/berkas_jarak_jauh}}`

- Salin suatu objek dalam S3 ke dalam ember lain:

`aws s3 cp s3://{{nama_ember1}}/{{jalan/menuju/berkas}} s3://{{nama_ember2}}/{{jalan/menuju/tujuan}}`

- Salin suatu objek S3 menuju ember lainnya dengan nama objek yang sama:

`aws s3 cp s3://{{nama_ember1}}/{{jalan/menuju/berkas}} s3://{{nama_ember2}}`

- Salin kumpulan objek S3 ke dalam suatu direktori lokal:

`aws s3 cp s3://{{nama_ember}} . --recursive`

- Tampilkan bantuan:

`aws s3 cp help`
