# rsync

> Transfer kumpulan berkas baik menuju atau dari suatu host jarak jauh (namun tidak antara dua host jarak jauh), secara konfigurasi bawaan menggunakan SSH.
> Untuk mendefinisikan suatu alamat sumber jarak jauh, gunakan `user@host:jalan/menuju/berkas_atau_direktori`.
> Informasi lebih lanjut: <https://download.samba.org/pub/rsync/rsync.1>.

- Transfer suatu berkas:

`rsync {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Gunakan mode arsip (salin direktori secara rekursif, salin tautan simbolik tanpa menyelesaikan, dan pertahankan izin, kepemilikan, dan waktu modifikasi):

`rsync {{[-a|--archive]}} {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Kompres data saat dikirim ke tujuan, tampilkan informasi kemajuan secara verbose dan dapat dibaca manusia, dan simpan sebagian file yang ditransfer jika terganggu:

`rsync {{[-zvhP|--compress --verbose --human-readable --partial --progress]}} {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Salin kumpulan direktori secara rekursif:

`rsync {{[-r|--recursive]}} {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Transfer isi direktori, tetapi bukan direktori itu sendiri:

`rsync {{[-r|--recursive]}} {{jalan/menuju/sumber/}} {{jalan/menuju/tujuan}}`

- Gunakan mode arsip, selesaikan tautan simbolik, dan lewati file yang lebih baru di tujuan:

`rsync {{[-auL|--archive --update --copy-links]}} {{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Transfer direktori dari host jarak jauh yang menjalankan `rsyncd` dan hapus file di tujuan yang tidak ada di sumber:

`rsync {{[-r|--recursive]}} --delete rsync://{{host}}:{{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`

- Transfer file melalui SSH menggunakan port yang berbeda dari default (22) dan tampilkan kemajuan proses secara global:

`rsync {{[-e|--rsh]}} 'ssh -p {{port}}' --info=progress2 {{host}}:{{jalan/menuju/sumber}} {{jalan/menuju/tujuan}}`
