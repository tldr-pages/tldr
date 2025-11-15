# ls

> Tampilkan daftar konten pada direktori.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html>.

- Tampilkan daftar isi berkas dengan satu item tiap baris:

`ls -1`

- Tampilkan daftar isi semua berkas, termasuk berkas tersembunyi:

`ls {{[-a|--all]}}`

- Tampilkan daftar isi semua berkas, dengan akhiran `/` ditambahkan ke nama direktori:

`ls {{[-F|--classify]}}`

- Tampilkan daftar isi berformat panjang (menampilkan izin, kepemilikan, ukuran dan waktu modifikasi pada setiap berkas):

`ls {{[-la|--all -l]}}`

- Tampilkan daftar isi berformat panjang dan ukuran ditampilkan menggunakan unit yang mudah dibaca manusia (KiB, MiB, GiB):

`ls {{[-lh|-l --human-readable]}}`

- Tampilkan daftar isi seluruh berkas secara rekursif, berformat panjang dan diurutkan berdasarkan ukuran (menurun):

`ls {{-lSR|-lS --recursive}}`

- Tampilkan daftar isi berformat panjang dari semua berkas dan diurutkan berdasarkan tanggal modifikasi (terlama dulu):

`ls {{[-ltr|-lt --reverse]}}`

- Hanya tampilkan daftar [d]irektori:

`ls {{[-d|--directory]}} */`
