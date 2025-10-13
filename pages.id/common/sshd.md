# sshd

> Secure Shell Daemon - mengizinkan mesin jarak jauh (remote host) untuk masuk (log in) secara aman ke mesin klien.
> Mesin jarak jauh dapat mengeksekusi perintah di mesin ini.
> Informasi lebih lanjut: <https://man.openbsd.org/sshd>.

- Mulai daemon di latar belakang (background):

`sshd`

- Jalankan sshd di latar depan (foreground):

`sshd -D`

- Jalankan dengan output verbose (untuk proses debug):

`sshd -D -d`

- Jalankan pada port tertentu:

`sshd -p {{port}}`
