# pkg_info

> Lihat dokumentasi mengenai paket yang tersedia baik dalam repositori atau pemasangan OpenBSD.
> Lihat juga: `pkg_add`, `pkg_delete`.
> Informasi lebih lanjut: <https://man.openbsd.org/pkg_info>.

- Cari detail paket yang tersedia dalam repositori menurut namanya:

`pkg_info -Q {{nama_paket}}`

- Tampilkan dan simpan daftar paket yang telah terpasang, untuk digunakan dalam `pkg_add -l`:

`pkg_info -mz`
