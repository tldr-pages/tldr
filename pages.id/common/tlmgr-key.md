# tlmgr key

> Atur daftar kunci GPG untuk memverifikasi pangkalan data paket TeX Live.
> Informasi lebih lanjut: <https://www.tug.org/texlive/doc/tlmgr.html#key>.

- Tampilkan seluruh kunci untuk TeX Live:

`tlmgr key list`

- Tambahkan suatu kunci dari berkas:

`sudo tlmgr key add {{jalan/menuju/kunci.gpg}}`

- Tambahkan suatu kunci dari `stdin`:

`cat {{jalan/menuju/kunci.gpg}} | sudo tlmgr key add -`

- Hapus suatu kunci menurut nomor induknya (ID):

`sudo tlmgr key remove {{id_kunci}}`
