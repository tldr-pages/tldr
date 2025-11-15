# agate

> Sebuah server sederhana untuk protokol jaringan Gemini.
> Informasi lebih lanjut: <https://github.com/mbrubeck/agate>.

- Terbitkan kunci privat dan sertifikat TLS:

`agate --content {{jalan/menuju/direktori_konten}} --addr {{[::]:1965}} --addr {{0.0.0.0:1965}} --hostname {{example.com}} --lang {{en-US}}`

- Jalankan server Gemini:

`agate {{jalan/menuju/direktori_konten}}`

- Tampilkan informasi bantuan:

`agate -h`
