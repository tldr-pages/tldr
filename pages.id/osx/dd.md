# dd

> Konversi dan salin file menuju media penyimpanan.
> Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/dd.1.html>.

- Buat suatu perangkat USB bootable dari suatu berkas isohybrid (seperti `archlinux-xxx.iso`) dan tampilkan kemajuannya:

`dd if={{jalan/menuju/berkas.iso}} of={{/dev/perangkat_usb}} status=progress`

- Salin isi suatu perangkat penyimpanan menuju perangkat lain dengan ukuran blok 4 MB, abaikan kesalahan, dan tampilkan kemajuannya:

`dd bs=4m conv=noerror if={{/dev/perangkat_asal}} of={{/dev/perangkat_tujuan}} status=progress`

- Buat suatu berkas berisikan byte acak dari perangkat pengacak dalam kernel dengan jumlah ukuran berkas yang ditentukan:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{jalan/menuju/berkas_acak}}`

- Ukur kinerja media penyimpanan dalam menulis data secara sekuensial:

`dd bs={{1024}} count={{1000000}}` `if=/dev/zero of={{jalan/menuju/berkas_1GB}}`

- Buat cadangan sistem, simpan ke dalam berkas IMG (dapat dipulihkan nanti dengan menukar `if` dan `of`), dan tampilkan kemajuannya:

`dd if={{/dev/perangkat_penyimpanan}} of={{jalan/menuju/berkas.img}} status=progress`

- Periksa kemajuan dari suatu proses `dd` yang sedang berjalan (jalankan perintah ini dari sesi shell lainnya):

`kill -USR1 $(pgrep ^dd)`
