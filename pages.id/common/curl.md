# curl

> Mentransfer data dari atau menuju suatu server.
> Mendukung sebagian besar protokol, termasuk HTTP, FTP, dan POP3.
> Informasi lebih lanjut: <https://curl.se/docs/manpage.html>.

- Buat suatu permintaan HTTP GET dan tampilkan respons menuju `stdout`:

`curl {{https://example.com}}`

- Buat suatu permintaan HTTP GET, ikuti (fo[L]low) seluruh permintaan redirect `3xx`, dan tampilkan ([D]ump) seluruh data header beserta isi respons menuju `stdout`:

`curl {{[-L|--location]}} {{[-D|--dump-header]}} - {{https://example.com}}`

- Unduh dan simpan suatu berkas dengan nama berkas yang ditentukan oleh URL:

`curl {{[-O|--remote-name]}} {{http://contoh.com/nama_berkas.zip}}`

- Kirim suatu [d]ata dengan format form-encoded (permintaan POST dengan format data `application/x-www-form-urlencoded`). Gunakan `--data @file_name` atau `--data @'-'` untuk membaca dari `stdin`:

`curl {{[-X|--request]}} POST {{[-d|--data]}} {{'name=bob'}} {{http://example.com/form}}`

- Kirim sebuah permintaan dengan suatu informasi header ekstra, menggunakan metode HTTP kustom yang dikirimkan menggunakan suatu pro[x]i (seperti BurpSuite), mengabaikan peringatan sertifikat TLS yang ditandatangani secara mandiri (self-signed):

`curl {{[-k|--insecure]}} {{[-x|--proxy]}} {{http://127.0.0.1:8080}} {{[-H|--header]}} {{'Authorization: Bearer token'}} {{[-X|--request]}} {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- Kirim data dalam format JSON, dengan menetapkan isi HTTP [H]eader Content-Type:

`curl {{[-d|--data]}} {{'{"name":"bob"}'}} {{[-H|--header]}} {{'Content-Type: application/json'}} {{http://example.com/pengguna/1234}}`

- Gunakan suatu sertifikat klien dan berkas kunci dalam mengenkripsi permintaan HTTP, dengan mengabaikan proses validasi sertifikat TLS:

`curl {{[-E|--cert]}} {{sertifikat_klien.pem}} --key {{kunci.pem}} {{[-k|--insecure]}} {{https://example.com}}`

- Ubah nama host menjadi alamat IP khusus, dengan keluaran [v]erbose (mirip dengan menyunting berkas `/etc/hosts` untuk resolusi DNS khusus):

`curl {{[-v|--verbose]}} --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
