# clamscan

> Sebuah program baris perintah untuk memindai virus komputer.
> Informasi lebih lanjut: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- Pindai kerentanan sebuah berkas:

`clamscan {{jalan/menuju/berkas}}`

- Pindai seluruh berkas dalam sebuah direktori secara rekursif:

`clamscan {{[-r|--recursive]}} {{jalan/menuju/direktori}}`

- Pindai data dari input `stdin`:

`{{perintah}} | clamscan -`

- Gunakan basis data (database) definisi virus yang terkandung dalam sebuah berkas atau direktori:

`clamscan {{[-d|--database]}} {{jalan/menuju/berkas_atau_direktori_basis_data}}`

- Pindai direktori saat ini dan hanya tampilkan berkas yang terinfeksi:

`clamscan {{[-i|--infected]}}`

- Simpan hasil laporan pemindaian kepada sebuah berkas log:

`clamscan {{[-l|--log]}} {{jalan/menuju/berkas_log}}`

- Pindahkan berkas-berkas yang terinfeksi kepada suatu direktori:

`clamscan --move {{jalan/menuju/direktori_karantina}}`

- Hapus berkas-berkas yang terinfeksi:

`clamscan --remove yes`
