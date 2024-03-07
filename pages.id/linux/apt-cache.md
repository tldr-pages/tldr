# apt-cache

> Pencari paket untuk Debian dan Ubuntu.
> Informasi lebih lanjut: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Cari paket di sumber yang sudah dimiliki:

`apt-cache search {{query}}`

- Tampilkan informasi tentang sebuah paket:

`apt-cache show {{paket}}`

- Tampilkan apakah sebuah paket sudah terinstal dan paling terbaru:

`apt-cache policy {{paket}}`

- Tampilkan dependensi sebuah paket:

`apt-cache depends {{paket}}`

- Tampilkan paket yang bergantung pada paket tertentu:

`apt-cache rdepends {{paket}}`
