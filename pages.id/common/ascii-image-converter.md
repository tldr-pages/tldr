# ascii-image-converter

> Ubah suatu gambar menjadi ASCII.
> Informasi lebih lanjut: <https://github.com/TheZoraiz/ascii-image-converter#cli-usage>.

- Ubah suatu gambar menjadi ASCII:

`ascii-image-converter {{jalan/menuju/gambar|URL}}`

- Tampilkan hasil ASCII secara berwarna:

`ascii-image-converter {{[-C|--color]}} {{jalan/menuju/gambar|URL}}`

- Buat gambar dengan ambang batas menggunakan huruf Braille (jika gambar hampir tidak terlihat, coba ubah font terminal):

`ascii-image-converter {{[-b|--braille]}} {{jalan/menuju/gambar|URL}}`

- Buat gambar dengan efek dithering menggunakan huruf Braille (jika gambar hampir tidak terlihat, coba ubah font terminal):

`ascii-image-converter {{[-b|--braille]}} --dither {{jalan/menuju/gambar|URL}}`

- Tampilkan gambar dengan warna negatif:

`ascii-image-converter {{[-Cn|--color --negative]}} {{jalan/menuju/gambar|URL}}`

- Gunakan rentang karakter yang lebih luas untuk menampilkan suatu gambar (dapat dipakai untuk memperbaiki akurasi gambar):

`ascii-image-converter {{[-c|--complex]}} {{jalan/menuju/gambar|URL}}`
