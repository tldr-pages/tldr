# exif

> Lihat dan ubah informasi metadata EXIF pada berkas-berkas JPEG.
> Informasi lebih lanjut: <https://manned.org/exif>.

- Tampilkan daftar informasi EXIF yang terdapat pada suatu berkas gambar:

`exif {{jalan/menuju/gambar.jpg}}`

- Tampilkan daftar jenis tag informasi EXIF dalam format tabel, termasuk apakah tag tersebut terdapat dalam suatu gambar:

`exif --list-tags --no-fixup {{gambar.jpg}}`

- Ekstrak gambar pratinjau (thumbnail) dari suatu gambar menuju `thumbnail.jpg`:

`exif --extract-thumbnail --output={{thumbnail.jpg}} {{gambar.jpg}}`

- Tampilkan isi mentahan terhadap tag metadata "Model" dalam suatu gambar:

`exif --ifd={{0}} --tag={{Model}} --machine-readable {{gambar.jpg}}`

- Ganti nilai tag metadata "Artist" menjadi John Smith, dan simpan perubahan menuju berkas baru di `new.jpg`:

`exif --output={{new.jpg}} --ifd={{0}} --tag="{{Artist}}" --set-value="{{John Smith}}" --no-fixup {{gambar.jpg}}`
