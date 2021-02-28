# curl

> Mentransfer data dari atau ke server.
> Mendukung sebagian besar protokol, termasuk HTTP, FTP, dan POP3.
> Informasi lebih lanjut: <https://curl.se>.

- Unduh konten URL ke file:

`curl {{http://contoh.com}} -o {{namafile}}`

- Unduh file, simpan hasilnya dengan nama file yang ditentukan oleh URL:

`curl -O {{http://contoh.com/namafile}}`

- Unduh file, mengikuti pengalihan [L] okasi, dan secara otomatis [C] melanjutkan transfer file sebelumnya:

`curl -O -L -C - {{http://contoh.com/filename}}`

- Mengirim data form yang telah di encode (permintaan POST atau tipe data `application/x-www-form-urlencoded`). Gunakan `-d @file_name` atau `-d @'-'` untuk membaca dari STDIN:

`curl -d {{'name=bob'}} {{http://contoh.com/form}}`

- Mengirim sebuah permintaan dengan header tambahan, menggunakan metode HTTP kustom:

`curl -H {{'X-My-Header: 123'}} -X {{PUT}} {{http://contoh.com}}`

- Mengirim data dalam format JSON, Menentukan jenis konten yang sesuai header:

`curl -d {{'{"name":"bob"}'}} -H {{'Content-Type: application/json'}} {{http://contoh.com/users/1234}}`

- Memberikan nama pengguna dan kata sandi untuk otentikasi server:

`curl -u myusername:mypassword {{http://contoh.com}}`

- Memberikan sertifikat klien dan kunci untuk sumber daya, melewati validasi sertifikat:

`curl --cert {{client.pem}} --key {{key.pem}} --insecure {{https://contoh.com}}`
