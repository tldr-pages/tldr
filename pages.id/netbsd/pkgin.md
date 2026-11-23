# pkgin

> Atur pemasangan paket `pkgsrc` dalam NetBSD.
> Informasi lebih lanjut: <https://pkgin.net/#usage>.

- Pasang sebuah paket:

`pkgin install {{paket}}`

- Hapus paket yang dipasang beserta penunjangnya (dependencies):

`pkgin remove {{paket}}`

- Perbarui seluruh paket yang terpasang:

`pkgin full-upgrade`

- Cari paket yang tersedia dalam repositori:

`pkgin search {{kata_kunci}}`

- Tampilkan daftar paket yang terpasang:

`pkgin list`

- Hapus paket-paket penunjang (dependencies) yang sudah tidak terpakai:

`pkgin autoremove`
