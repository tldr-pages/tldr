# svcadm

> Instansi untuk manipulasi hak akses layanan.
> Informasi lebih lanjut: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Izinkan sebuah servis yang ada dalam basis data servis:

`svcadm enable {{nama_servis}}`

- Larang servis:

`svcadm disable {{nama servis}}`

- Jalankan ulang sebuah servis yang berjalan:

`svcadm restart {{nama servis}}`

- Perintahkan servis untuk baca ulang berkas konfigurasi:

`svcadm refresh {{nama servis}}`

- Bersihkan sebuah servis dari kondisi perawatan dan perintahkan untuk berjalan:

`svcadm clear {{nama servis}}`
