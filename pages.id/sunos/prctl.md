# prctl

> Ambil atau atur sumber daya dari proses, tugas dan projek yang berjalan.
> Informasi lebih lanjut: <https://www.unix.com/man-page/sunos/1/prctl>.

- Periksa batas dan perizinan proses:

`prctl {{pid}}`

- Periksa batas dan perizinan proses dalam format yang dapat diurai mesin:

`prctl -P {{pid}}`

- Ambil batas spesifik dari sebuah proses yang berjalan:

`prctl -n process.max-file-descriptor {{pid}}`
