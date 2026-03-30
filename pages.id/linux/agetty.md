# agetty

> Alternatif `getty`: Buka sebuah port `tty`, minta nama login, dan jalankan perintah `/bin/login`.
> Biasanya dijalankan oleh `init`.
> Catatan: Baud rate adalah kecepatan transfer data antara terminal dan perangkat melalui koneksi serial.
> Informasi lebih lanjut: <https://manned.org/agetty>.

- Hubungkan `stdin` ke sebuah port (relatif terhadap `/dev`) dan secara opsional tentukan baud rate (secara bawaan 9600):

`agetty {{tty}} {{115200}}`

- Asumsikan `stdin` sudah terhubung ke sebuah `tty` dan atur timeout untuk login:

`agetty {{[-t|--timeout]}} {{timeout_in_seconds}} -`

- Asumsikan `tty` adalah 8-bit, menimpa variabel environment `$TERM` yang diatur oleh `init`:

`agetty {{[-8|--8bits]}} - {{term_var}}`

- Lewati proses login (tanpa login) dan jalankan program login lain sebagai root, alih-alih `/bin/login`:

`agetty {{[-n|--skip-login]}} {{[-l|--login-program]}} {{login_program}} {{tty}}`

- Jangan tampilkan file pra-login (issue) (`/etc/issue` secara bawaan) sebelum menuliskan prompt login:

`agetty {{[-i|--noissue]}} -`

- Ubah direktori root dan tulis host palsu tertentu ke dalam file `utmp`:

`agetty {{[-r|--chroot]}} /{{path/ke/root_directory}} {{[-H|--host]}} {{fake_host}} -`
