# pkg_add

> Pasang/perbarui paket dalam OpenBSD.
> Lihat juga: `pkg_info`, `pkg_delete`.
> Informasi lebih lanjut: <https://man.openbsd.org/pkg_add>.

- Perbarui seluruh paket yang terpasang, termasuk penunjangnya (dependencies):

`pkg_add -u`

- Pasang paket baru:

`pkg_add {{paket}}`

- Pasang paket menurut informasi paket yang dikeluarkan dari `pkg_info`:

`pkg_add -l {{jalan/menuju/file_hasil_pkg_info}}`
