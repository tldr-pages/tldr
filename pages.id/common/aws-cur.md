# aws cur

> Buat, cari, dan hapus definisi atau spesifikasi laporan penggunaan jasa AWS.
> Informasi lebih lanjut: <https://docs.aws.amazon.com/cli/latest/reference/cur/>.

- Buat suatu definisi laporan biaya dan penggunaan AWS dari berkas JSON:

`aws cur put-report-definition --report-definition file://{{jalan/menuju/definisi_laporan.json}}`

- Tampilkan daftar definisi laporan penggunaan yang didefinisikan untuk akun yang sedang masuk:

`aws cur describe-report-definitions`

- Hapus suatu definisi laporan penggunaan:

`aws cur --region {{wilayah_aws}} delete-report-definition --report-name {{laporan}}`
