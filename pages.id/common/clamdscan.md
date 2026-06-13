# clamdscan

> Sebuah program baris perintah untuk memindai virus komputer.
> Informasi lebih lanjut: <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>.

- Pindai kerentanan suatu berkas atau direktori tertentu:

`clamdscan {{jalan/menuju/berkas_atau_direktori}}`

- Pindai data dari input `stdin`:

`{{perintah}} | clamdscan -`

- Pindai direktori saat ini dan hanya tampilkan berkas yang terinfeksi:

`clamdscan --infected`

- Simpan hasil laporan pemindaian kepada sebuah berkas log:

`clamdscan --log {{jalan/menuju/berkas_log}}`

- Pindahkan berkas-berkas yang terinfeksi kepada suatu direktori:

`clamdscan --move {{jalan/menuju/direktori_karantina}}`

- Hapus berkas-berkas yang terinfeksi:

`clamdscan --remove`

- Gunakan lebih dari satu thread untuk memindai sebuah direktori:

`clamdscan --multiscan`

- Pindai berkas dengan memberikan deskriptor kepada daemon daripada mengoper isi mentah berkas tersebut seperti biasa:

`clamdscan --fdpass`
