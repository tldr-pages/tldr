# git archive

> Buat sebuah arsip direktori berdasarkan cabang/tree tertentu.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-archive>.

- Buat sebuah arsip tar berisikan isi dari tree HEAD saat ini, kemudian tampilkan isi file arsip mentah menuju `stdout`:

`git archive --verbose HEAD`

- Buat sebuah arsip zip dari tree HEAD saat ini, kemudian tampilkan isi file arsip mentah menuju `stdout`:

`git archive --verbose --format zip HEAD`

- Lakukan hal yang sama, namun simpan arsip zip ke dalam suatu direktori:

`git archive --verbose --output {{jalan/menuju/file.zip}} HEAD`

- Buat arsip tar dari komit terakhir pada cabang tertentu:

`git archive --output {{jalan/menuju/file.tar}} {{nama_cabang}}`

- Buat arsip tar berdasaran subdirektori tertentu pada suatu repositori Git:

`git archive --output {{jalan/menuju/file.tar}} HEAD:{{jalan/menuju/direktori}}`

- Bubuhkan nama jalur pada awal nama setiap file, untuk diarsipkan di dalam direktori tertentu:

`git archive --output {{jalan/menuju/file.tar}} --prefix {{jalan/untuk/dibubuhkan}}/ HEAD`
