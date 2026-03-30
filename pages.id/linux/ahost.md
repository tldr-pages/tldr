# ahost

> Utilitas pencarian DNS untuk menampilkan record A atau AAAA yang terkait dengan hostname atau alamat IP.
> Informasi lebih lanjut: <https://manned.org/ahost>.

- Tampilkan record `A` atau `AAAA` yang terkait dengan suatu hostname atau alamat IP:

`ahost {{example.com}}`

- Tampilkan output debugging tambahan:

`ahost -d {{example.com}}`

- Tampilkan record dengan tipe yang ditentukan:

`ahost -t {{a|aaaa|u}} {{example.com}}`
