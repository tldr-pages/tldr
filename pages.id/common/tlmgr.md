# tlmgr

> Atur pemasangan paket dan konfigurasi terhadap suatu instalasi TeX Live.
> Beberapa subperintah seperti `paper` mempunyai dokumentasi terpisah.
> Informasi lebih lanjut: <https://www.tug.org/texlive/doc/tlmgr.html#ACTIONS>.

- Pasang suatu paket beserta kumpulan paket kebergantungannya:

`tlmgr install {{paket}}`

- Hapus paket dan semua paket kebergantungannya:

`tlmgr remove {{paket}}`

- Tampilkan informasi tentang suatu paket:

`tlmgr info {{paket}}`

- Mutakhirkan seluruh paket:

`tlmgr update --all`

- Tampilkan daftar paket yang dapat diperbarui tanpa melakukan proses pemutakhiran:

`tlmgr update --list`

- Jalankan versi GUI dari program tlmgr:

`tlmgr gui`

- Tampilkan seluruh konfigurasi TeX Live:

`tlmgr conf`
