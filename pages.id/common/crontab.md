# crontab

> Jadwalkan tugas-tugas cron untuk dijalankan pada interval waktu bagi pengguna saat ini.
> Informasi lebih lanjut: <https://manned.org/crontab>.

- Sunting ([e]dit) berkas crontab untuk pengguna saat ini:

`crontab -e`

- Sunting berkas crontab untuk pengguna ([u]ser) tertentu:

`sudo crontab -e -u {{pengguna}}`

- Ganti seluruh isi crontab saat ini dengan isi dari berkas tertentu:

`crontab {{jalan/menuju/berkas}}`

- Tampilkan ([l]ist) daftar tugas cron untuk pengguna saat ini:

`crontab -l`

- Hapuskan ([r]emove) seluruh tugas cron untuk pengguna saat ini:

`crontab -r`

- Contoh tugas cron yang akan dijalankan pukul 10:00 setiap hari (* berarti nilai apapun):

`0 10 * * * {{perintah_untuk_dijalankan}}`

- Contoh tugas cron yang akan dijalankan setiap 10 menit:

`*/10 * * * * {{perintah_untuk_dijalankan}}`

- Contoh tugas cron yang akan menjalankan suatu naskah pada pukul 02:30 setiap Jumat:

`30 2 * * Fri /{{jalan/menuju/naskah.sh}}`
