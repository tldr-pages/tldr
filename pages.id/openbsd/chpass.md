# chpass

> Tambahkan atau ubah informasi dalam pangkalan data pengguna sistem operasi, termasuk syel masuk dan kata sandi.
> Lihat juga: `passwd`.
> Informasi lebih lanjut: <https://man.openbsd.org/chpass>.

- Tentukan syel masuk secara spsifik untuk pengguna saat ini secara interaktif:

`doas chpass`

- Tentukan [s]yel masuk secara spesifik untuk pengguna saat ini:

`doas chpass -s {{jalan/menuju/syel}}`

- Tentukan [s]yel masuk untuk suatu pengguna:

`doas chpass -s {{jalan/menuju/syel}} {{username}}`

- Tentukan suatu entri dalam pangkalan data pengguna dalam format `passwd`:

`doas chpass -a {{username:kata_sandi_terenkripsi:uid:gid:...}}`
