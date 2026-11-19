# unzip

> Ekstrak kumpulan berkas/direktori dari arsip-arsip Zip.
> Lihat juga: `zip`.
> Informasi lebih lanjut: <https://manned.org/unzip>.

- Ekstrak seluruh isi berkas/direktori dari suatu arsip menuju direktori saat ini:

`unzip {{jalan/menuju/arsip}}.zip`

- Ekstrak kumpulan berkas/direktori dari suatu arsip menuju direktori tujuan tertentu:

`unzip {{jalan/menuju/arsip}}.zip -d {{jalan/menuju/tujuan}}`

- Ekstrak kumpulan berkas/direktori dari suatu arsip menuju `stdout` beserta daftar nama berkas-berkas:

`unzip -c {{jalan/menuju/arsip}}.zip`

- Ekstrak suatu arsip yang dikemas dari Windows, memiliki nama berkas-berkas yang mengandung karakter non-ASCII (misalnya, karakter huruf Cina atau Jepang):

`unzip -O {{gbk}} {{jalan/menuju/arsip}}.zip`

- Tampilkan daftar isi suatu arsip tanpa mengekstraknya:

`unzip -l {{jalan/menuju/arsip}}.zip`

- Ekstrak beberapa berkas tertentu yang terkandung dalam suatu arsip menuju direktori, tanpa menghiraukan struktur direktori yang dapat pula diekstrak:

`unzip -j {{jalan/menuju/arsip}}.zip {{jalan/menuju/berkas1_dalam_arsip jalan/menuju/berkas2_dalam_arsip ...}}`
