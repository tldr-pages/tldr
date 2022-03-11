# dpkg

> Manajer paket Debian.
> Beberapa subperintah seperti `dpkg deb` memiliki dokumentasi penggunaannya sendiri.
> Informasi lebih lanjut: <https://manpages.debian.org/latest/dpkg/dpkg.html>.

- Memasang paket dari sebuah file DEB:

`dpkg -i {{jalan/menuju/file.deb}}`

- Menghapus pemasangan sebuah paket:

`dpkg -r {{nama_paket}}`

- Memperlihatkan daftar paket terinstal:

`dpkg -l {{pola}}`

- Memperlihatkan isi sebuah paket:

`dpkg -L {{nama_paket}}`

- Memperlihatkan isi sebuah paket lokal:

`dpkg -c {{jalan/menuju/file.deb}}`

- Mencari tahu paket yang memiliki sebuah file:

`dpkg -S {{nama_file}}`
