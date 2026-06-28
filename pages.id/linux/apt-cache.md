# apt-cache

> Alat pencari paket peranti lunak untuk untuk Debian dan Ubuntu.
> Informasi lebih lanjut: <https://manned.org/apt-cache>.

- Cari paket yang tersedia dengan nama atau deskripsi tertentu:

`apt-cache search {{kata_kunci}}`

- Tampilkan informasi tentang sebuah paket:

`apt-cache show {{nama_paket}}`

- Tampilkan apakah sebuah paket sudah terpasang dan paling terbaru:

`apt-cache policy {{nama_paket}}`

- Tampilkan dependensi sebuah paket:

`apt-cache depends {{nama_paket}}`

- Tampilkan paket yang bergantung pada paket tertentu:

`apt-cache rdepends {{nama_paket}}`
