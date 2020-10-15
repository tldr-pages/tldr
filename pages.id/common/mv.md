# mv

> Memindah atau menamai-ulang file dan direktori

- Memindahkan file ke lokasi yang baru:

`mv {{sumber}} {{target}}`

- Memindah tanpa meminta konfirmasi sebelum menimpa file yang sudah ada:

`mv -f {{sumber}} {{target}}`

- Meminta konfirmasi sebelum menimpa file yang sudah ada, apapun *file permissions*-nya

`mv -i {{sumber}} {{target}}`

- Jangan menimpa file yang sudah ada di direktori tujuan:

`mv -n {{sumber}} {{target}}`

- Memindahkan file dalam mode *verbose*, menampilkan file-file yang dipindahkan

`mv -v {{sumber}} {{target}}`
