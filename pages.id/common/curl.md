# curl

> Mentransfer data dari atau ke server.
> Mendukung sebagian besar protokol, termasuk HTTP, FTP, dan POP3.
> Informasi lebih lanjut: <https://curl.se/docs/manpage.html>.

- Unduh konten URL ke file:

`curl {{http://contoh.com}} --output {{namafile}}`

- Unduh file, simpan hasilnya dengan nama file yang ditentukan oleh URL:

`curl --remote-name {{http://contoh.com/namafile}}`

- Unduh file, mengikuti pengalihan lokasi, dan secara otomatis melanjutkan transfer file sebelumnya:

`curl --remote-name --location --continue-at - {{http://contoh.com/filename}}`

- Mengirim data form yang telah di encode (permintaan POST atau tipe data `application/x-www-form-urlencoded`). Gunakan `--data @file_name` atau `--data @'-'` untuk membaca dari STDIN:

`curl --data {{'name=bob'}} {{http://contoh.com/form}}`

- Mengirim sebuah permintaan dengan header tambahan, menggunakan metode HTTP kustom:

`curl --header {{'X-My-Header: 123'}} --request {{PUT}} {{http://contoh.com}}`

- Mengirim data dalam format JSON, Menentukan jenis konten yang sesuai header:

`curl --data {{'{"name":"bob"}'}} --header {{'Content-Type: application/json'}} {{http://contoh.com/users/1234}}`

- Memberikan nama pengguna dan kata sandi untuk otentikasi server:

`curl --user myusername:mypassword {{http://contoh.com}}`

- Memberikan sertifikat klien dan kunci untuk sumber daya, melewati validasi sertifikat:

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://contoh.com}}`
