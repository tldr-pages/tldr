# atq

> Tampilkan daftar pekerjaan yang dijadwalkan menggunakan perintah `at` atau `batch`.
> Informasi lebih lanjut: <https://manned.org/atq>.

- Tampilkan daftar pekerjaan terjadwal untuk pengguna saat ini:

`atq`

- Tampilkan daftar pekerjaan dari suatu daftar antrian (queue, setiap antrian memiliki nama berupa satu karakter seperti `a`):

`atq -q {{a}}`

- Tampilkan daftar pekerjaan terjadwal untuk seluruh pengguna (jalankan sebagai superuser):

`sudo atq`
