# clamdscan

> Sebuah program pemindai virus berbasis command-line.
> Informasi lebih lanjut: <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>.

- Pindai kerentanan suatu file atau direktori tertentu:

`clamdscan {{jalan/menuju/file_atau_direktori}}`

- Pindai data dari input `stdin`:

`{{perintah}} | clamdscan -`

- Pindai direktori saat ini dan hanya tampilkan file yang terinfeksi:

`clamdscan --infected`

- Simpan hasil laporan pemindaian kepada sebuah file log:

`clamdscan --log {{jalan/menuju/file_log}}`

- Pindahkan file-file yang terinfeksi kepada suatu direktori:

`clamdscan --move {{jalan/menuju/direktori_karantina}}`

- Hapus file-file yang terinfeksi:

`clamdscan --remove`

- Gunakan lebih dari satu thread untuk memindai sebuah direktori:

`clamdscan --multiscan`

- Pindai file dengan memberikan deskriptor kepada daemon daripada mengoper isi mentah file tersebut seperti biasa:

`clamdscan --fdpass`
