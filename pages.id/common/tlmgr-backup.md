# tlmgr backup

> Atur pengaturan pencadangan kumpulan paket TeX Live.
> Direktori pencadangan default ditentukan sebagaimana diatur dalam opsi `backupdir`, dan dapat didapatkan menggunakan `tlmgr option`.
> Informasi lebih lanjut: <https://www.tug.org/texlive/doc/tlmgr.html#backup>.

- Buat suatu pencadangan atas satu atau lebih banyak paket:

`tlmgr backup {{paket1 paket2 ...}}`

- Buat suatu pencadangan terhadap seluruh paket:

`tlmgr backup --all`

- Buat suatu pencadangan menuju suatu direktori kustom:

`tlmgr backup {{paket}} --backupdir {{jalan/menuju/direktori_pencadangan}}`

- Hapus hasil-hasil pencadangan terhadap satu atau lebih banyak paket:

`tlmgr backup clean {{paket1 paket2 ...}}`

- Hapus seluruh hasil pencadangan terhadap seluruh paket:

`tlmgr backup clean --all`
