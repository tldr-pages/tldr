# ftp

> Transfer kumpulan berkas secara interaktif antara perangkat komputer lokal dan perangkat peladen layanan FTP jarak jauh.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- Hubungkan diri menuju peladen FTP secara interaktif:

`ftp {{host}}`

- Masuk ke dalam sistem FTP sebagai pengguna anonim:

`ftp -A {{host}}`

- Matikan fitur login otomatis saat mengawali hubungan kepada peladen:

`ftp -n {{host}}`

- Jalankan suatu berkas yang berisikan daftar perintah FTP:

`ftp -s:{{jalan\menuju\berkas}} {{host}}`

- [Interactive] Unduh beberapa berkas (menggunakan ekspresi `glob`):


`mget {{*.png}}`

- [Interactive] Unggah beberapa berkas (menggunakan ekspresi `glob`):

`mput {{*.zip}}`

- [Interactive] Hapus beberapa berkas dari peladen jarak jauh:

`mdelete {{*.txt}}`

- Tampilkan bantuan:

`ftp --help`
