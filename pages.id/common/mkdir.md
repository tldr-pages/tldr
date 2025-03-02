# mkdir

> Buat dan atur hak akses atas sejumlah direktori.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html>.

- Buat sejumlah direktori baru secara spesifik:

`mkdir {{jalan/menuju/direktori1 jalan/menuju/direktori2 ...}}`

- Buat sejumlah direktori baru secara spesifik beserta induk-induknya, bila dibutuhkan:

`mkdir {{[-p|--parents]}} {{jalan/menuju/direktori1 jalan/menuju/direktori2 ...}}`

- Buat sejumlah direktori baru dengan konfigurasi hak akses tertentu:

`mkdir {{[-m|--mode]}} {{rwxrw-r--}} {{jalan/menuju/direktori1 jalan/menuju/direktori2 ...}}`
