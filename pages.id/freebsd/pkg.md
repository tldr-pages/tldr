# pkg

> Manajer paket untuk FreeBSD.
> Informasi lebih lanjut: <https://man.freebsd.org/cgi/man.cgi?query=pkg&sektion=8>.

- Pasang sebuah paket:

`pkg install {{nama_paket}}`

- Hapus pemasangan paket:

`pkg delete {{nama_paket}}`

- Perbarui seluruh paket yang terpasang ke dalam versi terbaru:

`pkg upgrade`

- Cari paket yang tersedia dalam repositori:

`pkg search {{kata_kunci}}`

- Tampilkan daftar paket yang terpasang:

`pkg info`

- Hapus paket penunjang (dependency) yang sudah tidak dipakai:

`pkg autoremove`
