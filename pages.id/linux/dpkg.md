# dpkg

> Manajer paket Debian.
> Beberapa subperintah seperti `dpkg deb` memiliki dokumentasi penggunaannya sendiri.
> Informasi lebih lanjut: <https://manned.org/dpkg>.

- Pasang paket dari sebuah berkas DEB:

`dpkg -i {{jalan/menuju/berkas.deb}}`

- Hapus pemasangan sebuah paket:

`dpkg -r {{nama_paket}}`

- Tampilkan daftar paket terinstal:

`dpkg -l {{pola}}`

- Tampilkan rincian isi suatu paket:

`dpkg -L {{nama_paket}}`

- Tampilkan rincian isi berkas sebuah paket lokal:

`dpkg -c {{jalan/menuju/berkas.deb}}`

- Cari tahu paket yang memiliki sebuah berkas:

`dpkg -S {{nama_berkas}}`

- Hapus pemasangan paket beserta berkas konfigurasi yang dibentuk oleh paket tersebut:

`sudo dpkg {{[-P|--purge]}} {{nama_paket}}`
