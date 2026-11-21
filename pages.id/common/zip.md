# zip

> Kemas dan kompres (arsipkan) berkas-berkas menjadi sebuah arsip Zip.
> Lihat juga: `unzip`.
> Informasi lebih lanjut: <https://manned.org/zip>.

- Tambahkan kumpulan berkas dan direktori ke dalam suatu arsip:

`zip {{[-r|--recurse-paths]}} {{jalan/menuju/berkas_terkompres.zip}} {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}}`

- Hapus kumpulan berkas/direktori dari suatu arsip:

`zip {{[-d|--delete]}} {{jalan/menuju/berkas_terkompres.zip}} {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}}`

- Arsipkan kumpulan berkas/direktori kecuali berkas/direktori tertentu:

`zip {{[-r|--recurse-paths]}} {{jalan/menuju/berkas_terkompres.zip}} {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}} {{[-x|--exclude]}} {{path/to/excluded_files_or_directories}}`

- Arsipkan kumpulan berkas/direktori dengan tingkat kompresi tertentu (`0` - terendah, `9` - tertinggi):

`zip {{[-r|--recurse-paths]}} -{{0..9}} {{jalan/menuju/berkas_terkompres.zip}} {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}}`

- Buat sebuah berkas arsip yang disandikan menggunakan kata sandi tertentu:

`zip {{[-re|--recurse-paths --encrypt]}} {{jalan/menuju/berkas_terkompres.zip}} {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}}`

- Arsipkan kumpulan berkas/direktori menjadi runtutan berkas arsip Zip berseri / multi-part (misalnya, pecahkan arsip berkas menjadi kumpulan berkas berbobot 3 GB):

`zip {{[-rs|--recurse-paths --split-size]}} {{3g}} {{jalan/menuju/berkas_terkompres.zip}} {{jalan/menuju/berkas_atau_direktori1 jalan/menuju/berkas_atau_direktori2 ...}}`

- Cetak daftar isi suatu berkas:

`zip {{[-sf|--split-size --freshen]}} {{jalan/menuju/berkas_terkompres.zip}}`
