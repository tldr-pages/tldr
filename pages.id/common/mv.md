# mv

> Memindah atau menamai-ulang file dan direktori.

- Memindahkan file ke lokasi yang baru:

`mv {{sumber}} {{tujuan}}`

- Memindah tanpa meminta konfirmasi sebelum menimpa file yang sudah ada:

`mv -f {{sumber}} {{tujuan}}`

- Meminta konfirmasi sebelum menimpa file yang sudah ada, apapun *file permissions*-nya:

`mv -i {{sumber}} {{tujuan}}`

- Jangan menimpa file yang sudah ada di direktori tujuan:

`mv -n {{sumber}} {{tujuan}}`

- Memindahkan file dalam mode *verbose*, menampilkan file-file yang dipindahkan:

`mv -v {{sumber}} {{tujuan}}`
