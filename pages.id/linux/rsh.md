# rsh

> Jalankan kumpulan perintah pada suatu host jarak jauh.
> Informasi lebih lanjut: <https://www.gnu.org/software/inetutils/manual/inetutils.html#rsh-invocation>.

- Jalankan sebuah perintah pada suatu host jarak jauh:

`rsh {{host_jarak_jauh}} {{ls -l}}`

- Jalankan perintah pada host jarak jauh dengan nama pengguna (username) tertentu:

`rsh {{host_jarak_jauh}} {{[-l|--user]}} {{nama_pengguna}} {{ls -l}}`

- Alihkan `stdin` menuju `/dev/null` saat menjalankan perintah pada host jarak jauh:

`rsh {{host_jarak_jauh}} --no-err {{ls -l}}`
