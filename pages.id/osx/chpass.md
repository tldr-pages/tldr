# chpass

> Tambahkan atau ubah informasi dalam pangkalan data pengguna sistem operasi, termasuk syel masuk dan kata sandi.
> Catatan: Kata sandi pengguna tidak dapat diubah pada sistem Open Directory, gunakan `passwd` sebagai gantinya.
> Lihat juga: `passwd`.
> Informasi lebih lanjut: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Tentukan syel masuk secara spsifik untuk pengguna saat ini secara interaktif:

`chpass`

- Tentukan [s]yel masuk secara spesifik untuk pengguna saat ini:

`chpass -s {{jalan/menuju/syel}}`

- Tentukan [s]yel masuk untuk suatu pengguna:

`chpass -s {{jalan/menuju/syel}} {{username}}`

- Ubah rekam pengguna dalam node direktori pada [l]okasi yang ditentukan:

`chpass -l {{lokasi}} -s {{jalan/menuju/syel}} {{username}}`

- Gunakan suatu nama pengguna ([u]sername) saat melakukan proses masuk menuju node direktori yang memiliki informasi pengguna:

`chpass -u {{username_untuk_autentikasi}} -s {{path/to/shell}} {{username_sesungguhnya}}`
