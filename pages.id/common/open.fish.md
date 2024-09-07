# open

> Buka file, direktori, dan alamat URI dengan aplikasi-aplikasi default yang dapat membukanya.
> Perintah ini tersedia melalui fish dalam sistem operasi yang tidak menawarkan perintah `open` secara bawaan (seperti Haiku dan macOS).
> Informasi lebih lanjut: <https://fishshell.com/docs/current/cmds/open.html>.

- Buka sebuah file di dalam aplikasi default:

`open {{file.ext}}`

- Buka semua file dengan ekstensi tertentu di dalam aplikasi default pada direktori saat ini:

`open {{*.ext}}`

- Buka sebuah direktori di dalam aplikasi manajer file default:

`open {{jalan/menuju/direktori}}`

- Buka sebuah situs web di dalam aplikasi peramban default:

`open {{https://example.com}}`

- Buka sebuah alamat URI di dalam aplikasi default yang dapat menanganinya:

`open {{tel:123}}`
