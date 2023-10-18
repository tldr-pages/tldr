# mv

> Memindah atau menamai-ulang file dan direktori.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/mv>.

- Memindahkan file ke lokasi yang baru:

`mv {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Memindah tanpa meminta konfirmasi sebelum menimpa file yang sudah ada:

`mv -f {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Meminta konfirmasi sebelum menimpa file yang sudah ada, apapun *file permissions*-nya:

`mv -i {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Jangan menimpa file yang sudah ada di direktori tujuan:

`mv -n {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Memindahkan file dalam mode *verbose*, menampilkan file-file yang dipindahkan:

`mv -v {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`
