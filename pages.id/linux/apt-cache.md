# apt-cache

> Alat query paket untuk Debian dan Ubuntu.
> Informasi lebih lanjut: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Mencari paket di sumber yang sudah kamu miliki:

`apt-cache search {{query}}`

- Menampilkan informasi tentang sebuah paket:

`apt-cache show {{package}}`

- Menampilkan apakah sebuah paket sudah terinstal dan paling terbaru:

`apt-cache policy {{package}}`

- Menampilkan dependensi sebuah paket:

`apt-cache depends {{package}}`

- Menampilkan paket yang bergantung pada paket tertentu:

`apt-cache rdepends {{package}}`
