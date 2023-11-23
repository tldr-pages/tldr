# clamscan

> Sebuah program pemindai virus berbasis command-line.
> Informasi lebih lanjut: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- Pindai kerentanan sebuah file:

`clamscan {{jalan/menuju/file}}`

- Pindai seluruh file dalam sebuah direktori secara rekursif:

`clamscan -r {{jalan/menuju/direktori}}`

- Pindai data dari input `stdin`:

`{{perintah}} | clamscan -`

- Gunakan basis data (database) definisi virus yang terkandung dalam sebuah file atau direktori:

`clamscan --database {{jalan/menuju/file_atau_direktori_basis_data}}`

- Pindai direktori saat ini dan hanya tampilkan file yang terinfeksi:

`clamscan --infected`

- Simpan hasil laporan pemindaian kepada sebuah file log:

`clamscan --log {{jalan/menuju/file_log}}`

- Pindahkan file-file yang terinfeksi kepada suatu direktori:

`clamscan --move {{jalan/menuju/direktori_karantina}}`

- Hapus file-file yang terinfeksi:

`clamscan --remove`
