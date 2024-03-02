# apt-cache

> Pencari paket untuk Debian dan Ubuntu.
> Informasi lebih lanjut: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Mencari paket di sumber yang sudah kamu miliki:

`apt-cache search {{query}}`

- Menampilkan informasi tentang sebuah paket:

`apt-cache show {{paket}}`

- Menampilkan apakah sebuah paket sudah terinstal dan paling terbaru:

`apt-cache policy {{paket}}`

- Menampilkan dependensi sebuah paket:

`apt-cache depends {{paket}}`

- Menampilkan paket yang bergantung pada paket tertentu:

`apt-cache rdepends {{paket}}`
