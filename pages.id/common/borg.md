# borg

> Alat pencadangan bebas duplikat.
> Buat cadangan berkas lokal dan jarak jauh yang dapat dimuat sebagai sistem penyimpanan.
> Informasi lebih lanjut: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- Inisialisasikan suatu repositori (atau repositori lokal):

`borg init {{jalan/menuju/direktori_repo}}`

- Cadangkan suatu direktori ke dalam repositori dengan nama arsip "Senin":

`borg create --progress {{jalan/menuju/direktori_repo}}::{{Senin}} {{jalan/menuju/direktori_sumber}}`

- Tampilkan daftar seluruh arsip yang dikelola dalam suatu repositori:

`borg list {{jalan/menuju/direktori_repo}}`

- Ekstrak isi suatu direktori dalam arsip "Senin" dalam suatu repositori jarak jauh, kecuali seluruh berkas bernama `*.ext`:

`borg extract {{pengguna}}@{{host}}:{{jalan/menuju/direktori_repo}}::{{Senin}} {{jalan/menuju/direktori_target}} --exclude '{{*.ext}}'`

- Pangkas suatu repositori dengan membuang kumpulan arsip yang dibuat lebih dari 7 hari lalu, dengan menampilkan daftar perubahannya:

`borg prune --keep-within {{7d}} --list {{jalan/menuju/direktori_repo}}`

- Muat suatu repositori sebagai sistem penyimpanan FUSE:

`borg mount {{jalan/menuju/direktori_repo}}::{{Senin}} {{jalan/menuju/titik_muat}}`

- Tampilkan informasi bantuan mengenai pembuatan arsip:

`borg create --help`
