# acme.sh

> Sebuah shell script yang mengimplementasikan ACME client protocol (pembuat sertifikat HTTPS), alternatif dari `certbot`.
> Lihat juga: `acme.sh dns`.
> Informasi lebih lanjut: <https://github.com/acmesh-official/acme.sh#2-just-issue-a-cert>.

- Terbitkan sertifikat baru dan pasang pada webroot secara langsung:

`acme.sh --issue {{[-d|--domain]}} {{example.com}} {{[-w|--webroot]}} /{{jalan/menuju/webroot}}`

- Terbitkan sertifikat untuk domain majemuk, menggunakan mode verifikasi mandiri (standalone) pada port 80:

`acme.sh --issue --standalone {{[-d|--domain]}} {{example.com}} {{[-d|--domain]}} {{www.example.com}}`

- Terbitkan sertifikat menggunakan mode verifikasi mandiri berbasis TLS pada port 443:

`acme.sh --issue --alpn {{[-d|--domain]}} {{example.com}}`

- Terbitkan sertifikat dengan konfigurasi server `nginx` untuk memasangnya:

`acme.sh --issue --nginx {{[-d|--domain]}} {{example.com}}`

- Terbitkan sertifikat dengan konfigurasi server Apache untuk memasangnya:

`acme.sh --issue --apache {{[-d|--domain]}} {{example.com}}`

- Terbitkan sertifikat wildcard (\*) menggunakan mode verifikasi DNS via API secara otomatis:

`acme.sh --issue --dns {{api_dns}} {{[-d|--domain]}} {{*.example.com}}`

- Pasang sertifikat ke dalam direktori tertentu (dapat berguna untuk proses pemutakhiran otomatis):

`acme.sh {{[-i|--install-cert]}} {{[-d|--domain]}} {{example.com}} --key-file /{{jalan/menuju/example.com.key}} --fullchain-file /{{jalan/menuju/example.com.cer}} --reloadcmd "{{systemctl force-reload nginx}}"`
