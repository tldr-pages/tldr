# exif

> Lihat dan ubah informasi metadata EXIF pada berkas-berkas JPEG.
> Informasi lebih lanjut: <https://manned.org/exif>.

- Tampilkan daftar informasi EXIF yang terdapat pada suatu berkas gambar:

`exif {{jalan/menuju/gambar.jpg}}`

- Tampilkan daftar jenis tag informasi EXIF dalam format tabel, termasuk apakah tag tersebut terdapat dalam suatu gambar:

`exif {{[-l|--list-tags]}} --no-fixup {{gambar.jpg}}`

- Ekstrak gambar pratinjau (thumbnail) dari suatu gambar menuju `thumbnail.jpg`:

`exif {{[-e|--extract-thumbnail]}} {{[-o|--output]}} {{thumbnail.jpg}} {{gambar.jpg}}`

- Tampilkan isi mentahan terhadap tag metadata "Model" dalam suatu gambar:

`exif --ifd {{0}} {{[-t|--tag]}} "Model" {{[-m|--machine-readable]}} {{gambar.jpg}}`

- Ganti nilai tag metadata "Artist" menjadi John Smith, dan simpan perubahan menuju berkas baru di `new.jpg`:

`exif {{[-o|--output]}} {{new.jpg}} --ifd {{0}} {{[-t|--tag]}} "Artist" --set-value "John Smith" --no-fixup {{gambar.jpg}}`
