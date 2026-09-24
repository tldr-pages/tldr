# apt-file

> Cari kumpulan berkas di dalam paket `apt`, termasuk yang belum dipasang.
> Informasi lebih lanjut: <https://manned.org/apt-file>.

- Perbarui basis data metadata:

`sudo apt update`

- Cari paket yang berisi nama atau lokasi berkas tertentu:

`apt-file {{[find|search]}} {{sebagian_nama_jalan/menuju/berkas}}`

- Tampilkan daftar konten dari sebuah paket:

`apt-file list {{paket}}`

- Cari paket yang sesuai dengan `ekspresi_reguler`:

`apt-file {{[find|search]}} {{[-x|--regexp]}} {{ekspresi_reguler}}`
