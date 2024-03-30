# acme.sh

> Sebuah shell script yang mengimplementasikan ACME client protocol (pembuat sertifikat HTTPS), alternatif dari `certbot`.
> Lihat juga: `acme.sh dns`.
> Informasi lebih lanjut: <https://github.com/acmesh-official/acme.sh>.

- Terbitkan sertifikat baru dan pasang pada webroot secara langsung:

`acme.sh --issue --domain {{example.com}} --webroot {{/jalan/menuju/webroot}}`

- Terbitkan sertifikat untuk domain majemuk, menggunakan mode verifikasi mandiri (standalone) pada port 80:

`acme.sh --issue --standalone --domain {{example.com}} --domain {{www.example.com}}`

- Terbitkan sertifikat menggunakan mode verifikasi mandiri berbasis TLS pada port 443:

`acme.sh --issue --alpn --domain {{example.com}}`

- Terbitkan sertifikat dengan konfigurasi server Nginx untuk memasangnya:

`acme.sh --issue --nginx --domain {{example.com}}`

- Terbitkan sertifikat dengan konfigurasi server Apache untuk memasangnya:

`acme.sh --issue --apache --domain {{example.com}}`

- Terbitkan sertifikat wildcard (\*) menggunakan verifikasi DNS via API (daftar jenis `api_dns` yang didukung tersedia dalam <https://github.com/acmesh-official/acme.sh/wiki/How-to-use-lexicon-DNS-API>):

`acme.sh --issue --dns {{api_dns}} --domain {{*.example.com}}`

- Pasang sertifikat ke dalam direktori tertentu (dapat berguna untuk proses pemutakhiran otomatis):

`acme.sh --install-cert -d {{example.com}} --key-file {{/jalan/menuju/example.com.key}} --fullchain-file {{/jalan/menuju/example.com.cer}} --reloadcmd {{"systemctl force-reload nginx"}}`
