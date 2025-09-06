# aws s3

> Alat baris perintah (CLI) untuk AWS S3 - jasa penyimpanan berkas bagi layanan web.
> Beberapa subperintah seperti `cp` mempunyai dokumentasi terpisah.
> Informasi lebih lanjut: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Tampilkan daftar seluruh berkas dalam suatu bucket:

`aws s3 ls {{nama_bucket}}`

- Lakukan sinkronisasi isi berkas dan direktori dari sumber penyimpanan lokal menuju suatu bucket:

`aws s3 sync {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}} s3://{{nama_bucket}}`

- Lakukan sinkronisasi isi berkas dan direktori dari suatu bucket menuju sumber penyimpanan lokal:

`aws s3 sync s3://{{nama_bucket}} {{jalan/menuju/tujuan}}`

- Lakukan sinkronisasi dengan pengecualian:

`aws s3 sync {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}} s3://{{bucket_name}} --exclude {{jalan/menuju/berkas}} --exclude {{jalan/menuju/direktori}}/*`

- Hapus suatu berkas dari suatu bucket:

`aws s3 rm s3://{{bucket}}/{{jalan/menuju/berkas}}`

- Hanya tampilkan daftar berkas yang dirubah tanpa melakukan perubahan tersebut (mode dry-run):

`aws s3 {{perintah}} --dryrun`
