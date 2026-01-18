# dpkg

> Manajer paket Debian.
> Beberapa subperintah seperti `deb` memiliki dokumentasi terpisah.
> Informasi lebih lanjut: <https://manned.org/dpkg>.

- Pasang suatu paket:

`sudo dpkg {{[-i|--install]}} {{jalan/menuju/berkas.deb}}`

- Hapus pemasangan sebuah paket:

`sudo dpkg {{[-r|--remove]}} {{nama_paket}}`

- Tampilkan daftar paket yang terpasang:

`dpkg {{[-l|--list]}} {{pola_atau_kata_kunci_pencarian}}`

- Lihat isi suatu paket:

`dpkg {{[-L|--listfiles]}} {{nama_paket}}`

- Lihat isi sebuah paket dari berkas lokal:

`dpkg {{[-c|--contents]}} {{jalan/menuju/berkas.deb}}`

- Cari tahu paket mana yang memiliki suatu berkas sistem:

`sudo dpkg {{[-S|--search]}} {{jalan/menuju/berkas}}`

- Hapus seluruh sisa data pemasangan paket, termasuk konfigurasi paket terhapus yang masih tersimpan:

`sudo dpkg {{[-P|--purge]}} {{nama_paket}}`
