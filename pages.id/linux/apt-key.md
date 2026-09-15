# apt-key

> Alat manajer kunci enkripsi untuk melakukan verifikasi paket dalam Manager Paket APT untuk Debian dan Ubuntu.
> Catatan: Program `apt-key` telah usang (kecuali perintah `apt-key del` dalam skrip manajemen sistem komputer).
> Informasi lebih lanjut: <https://manned.org/apt-key>.

- Tampilkan kumpulan kunci publik yang dipercayai dalam pemasangan sistem operasi:

`apt-key list`

- Tambahkan suatu kunci dari suatu berkas ke dalam daftar kunci terpercaya:

`apt-key add {{berkas_kunci_publik.asc}}`

- Hapus suatu kunci dari daftar kunci terpercaya:

`apt-key del {{key_id}}`

- Tambahkan suatu kunci dari sumber jaringan komputer ke dalam daftar kunci terpercaya:

`wget {{[-qO|--quiet --output-document]}} - {{https://host.tld/nama_berkas_kunci.key}} | apt-key add -`

- Tambahkan suatu kunci menggunakan nomor induk (Key ID) dari suatu peladen kunci ke dalam daftar kunci terpercaya:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{nomor_induk_kunci}}`
