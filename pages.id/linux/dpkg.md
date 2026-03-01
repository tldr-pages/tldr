# dpkg

> Manajer paket Debian.
> Beberapa subperintah seperti `dpkg deb` memiliki dokumentasi penggunaannya sendiri.
> Lihat <https://wiki.archlinux.org/title/Pacman/Rosetta> untuk daftar perintah dalam manajer paket lain yang menyerupai perintah `dpkg`.
> Informasi lebih lanjut: <https://manned.org/dpkg>.

- Pasang paket dari sebuah berkas DEB:

`sudo dpkg {{[-i|--install]}} {{jalan/menuju/berkas.deb}}`

- Hapus pemasangan sebuah paket:

`sudo dpkg {{[-r|--remove]}} {{nama_paket}}`

- Tampilkan daftar paket terinstal:

`dpkg {{[-l|--list]}} {{pola}}`

- Tampilkan rincian isi suatu paket:

`dpkg {{[-L|--listfiles]}} {{nama_paket}}`

- Tampilkan rincian isi berkas sebuah paket lokal:

`dpkg {{[-c|--contents]}} {{jalan/menuju/berkas.deb}}`

- Cari tahu paket yang memiliki sebuah berkas:

`dpkg {{[-S|--search]}} {{jalan/menuju/berkas}}`

<!-- - Hapus pemasangan paket beserta berkas konfigurasi yang dibentuk oleh paket tersebut: -->

`sudo dpkg {{[-P|--purge]}} {{nama_paket}}`
