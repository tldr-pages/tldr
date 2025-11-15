# pm2

> Manajer proses untuk Node.js.
> Digunakan untuk manajemen log, pemantauan, dan pengaturan proses.
> Informasi lebih lanjut: <https://pm2.keymetrics.io>.

- Memulai prooses dengan nama yang dapat digunakan untuk operasi selanjutnya:

`pm2 start {{app.js}} --name {{nama_aplikasi}}`

- Tampilkan daftar proses:

`pm2 list`

- Pantau semua proses:

`pm2 monit`

- Menghentikan sebuah proses:

`pm2 stop {{nama_aplikasi}}`

- Memulai ulang sebuah proses:

`pm2 restart {{nama_aplikasi}}`

- Membuang semua proses dan menghidupkan mereka kembali nanti:

`pm2 save`

- Menghidupkan kembali proses yang sebelumnya dibuang:

`pm2 resurrect`
