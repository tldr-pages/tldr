# aspell

> Mesin pengecek ejaan secara interaktif.
> Informasi lebih lanjut: <http://aspell.net/man-html/index.html>.

- Lakukan pengecekan ejaan terhadap suatu berkas:

`aspell check {{jalan/menuju/berkas}}`

- Tampilkan daftar kata dalam `stdin` yang dicurigai memiliki kesalahan ejaan:

`cat {{jalan/menuju/berkas}} | aspell list`

- Tampilkan daftar kamus dan bahasa yang didukung:

`aspell dicts`

- Jalankan `aspell` dengan bahasa teks yang berbeda (menggunakan format kode bahasa ISO 639):

`aspell --lang={{cs}}`

- Tampilkan daftar kata dalam `stdin` yang dicurigai memiliki kesalahan ejaan dan abaikan kata yang berasal dari daftar kata pribadi (personal word list):

`cat {{jalan/menuju/berkas}} | aspell --personal={{daftar-kata-pribadi.pws}} list`
