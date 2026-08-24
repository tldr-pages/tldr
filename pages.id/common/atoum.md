# atoum

> Kerangka pengujian unit program PHP yang sederhana, modern, dan intuitif.
> Informasi lebih lanjut: <https://atoum.readthedocs.io/en/latest/option_cli.html>.

- Inisialisasikan proyek dengan berkas konfigurasi baru:

`atoum --init`

- Jalankan seluruh ujian:

`atoum`

- Jalankan ujian dengan berkas konfigurasi tertentu:

`atoum {{[-c|--configuration]}} {{jalan/menuju/berkas}}`

- Jalankan ujian dari suatu berkas:

`atoum {{[-f|--files]}} {{jalan/menuju/berkas}}`

- Jalankan ujian dari suatu kumpulan direktori:

`atoum {{[-d|--directories]}} {{jalan/menuju/direktori}}`

- Jalankan seluruh ujian dengan namespace spesifik:

`atoum {{[-ns|--namespaces]}} {{namespace}}`

- Jalankan seluruh ujian dengan tag spesifik:

`atoum {{[-t|--tags]}} {{tag}}`

- Gunakan suatu berkas bootstrap sebelum menjalankan berkas:

`atoum {{[-bf|--bootstrap-file]}} {{jalan/menuju/berkas}}`
