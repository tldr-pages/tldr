# chpass

> Tambahkan atau ubah informasi dalam pangkalan data pengguna sistem operasi, termasuk syel masuk dan kata sandi.
> Lihat juga: `passwd`.
> Informasi lebih lanjut: <https://man.netbsd.org/chpass>.

- Tentukan syel masuk secara spsifik untuk pengguna saat ini secara interaktif:

`su -c chpass`

- Tentukan [s]yel masuk secara spesifik untuk pengguna saat ini:

`chpass -s {{jalan/menuju/syel}}`

- Tentukan [s]yel masuk untuk suatu pengguna:

`chpass -s {{jalan/menuju/syel}} {{username}}`

- Tentukan suatu entri dalam pangkalan data pengguna dalam format `passwd`:

`su -c 'chpass -a {{username:kata_sandi_terenkripsi:uid:gid:...}} -s {{jalan/menuju/syel}}' {{username}}`

- Hanya perbarui berkas kata sandi [l]okal:

`su -c 'chpass -l -s {{jalan/menuju/syel}}' {{username}}`

- Ubah entri pangkalan data kata sandi [y]P secara paksa:

`su -c 'chpass -y -s {{jalan/menuju/syel}}' {{username}}`
