# aws lambda

> Gunakan AWS Lambda, suatu layanan komputasi untuk menjalankan kode perintah tanpa membuat atau mengatur infrastruktur peladen.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- Jalankan suatu function:

`aws lambda invoke --function-name {{nama}} {{jalan/menuju/respons.json}}`

- Jalankan suatu function dengan payload masukan (input) dalam format JSON:

`aws lambda invoke --function-name {{nama}} --payload {{json}} {{jalan/menuju/respons.json}}`

- Tampilkan daftar function yang tersedia:

`aws lambda list-functions`

- Tampilkan informasi konfigurasi mengenai suatu function:

`aws lambda get-function-configuration --function-name {{nama}}`

- Tampilkan daftar alias yang didaftarkan terhadap suatu function:

`aws lambda list-aliases --function-name {{nama}}`

- Tampilkan informasi konfigurasi konkurensi yang dicadangkan (reserved concurrency) terhadap suatu function:

`aws lambda get-function-concurrency --function-name {{nama}}`

- Tampilkan daftar layanan AWS yang berhak memanggil suatu function:

`aws lambda get-policy --function-name {{nama}}`
