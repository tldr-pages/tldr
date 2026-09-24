# black

> Tulis ulang kode program Python secara otomatis.
> Lihat juga: `ruff`.
> Informasi lebih lanjut: <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html>.

- Tulis ulang kode dalam suatu berkas atau direktori:

`black {{jalan/menuju/berkas_atau_direktori}}`

- Tulis ulang kode yang dimasukkan sebagai teks string:

`black {{[-c|--code]}} "{{kode}}"`

- Tampilkan apakah isi kode suatu berkas atau direktori akan ditulis ulang atau tidak:

`black --check {{jalan/menuju/berkas_atau_direktori}}`

- Tampilkan daftar perubahan penulisan kode pada berkas atau direktori tanpa menjalankannya (dry-run):

`black --diff {{jalan/menuju/berkas_atau_direktori}}`

- Lakukan penulisan ulang dan hanya keluarkan pesan galat dalam `stderr`:

`black {{[-q|--quiet]}} {{jalan/menuju/berkas_atau_direktori}}`

- Lakukan penulisan ulang namun jangan menggantikan tanda petik tunggal menuju ganda (pembantu adopsi gaya penulisan bahasa Python berbasis Black, hindari menggunakan ini untuk proyek baru):

`black {{[-S|--skip-string-normalization]}} {{jalan/menuju/berkas_atau_direktori}}`
