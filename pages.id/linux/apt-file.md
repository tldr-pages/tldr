# apt-file

> Cari kumpulan berkas di dalam paket `apt`, termasuk yang belum dipasang.
> Informasi lebih lanjut: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Perbarui basis data metadata:

`sudo apt update`

- Cari paket yang berisi nama file atau path yang diinputkan:

`apt-file {{search|find}} {{path/ke/sebuah/file}}`

- Tampilkan daftar konten dari sebuah paket:

`apt-file {{show|list}} {{paket}}`

- Mencari paket yang yang sesuai dengan `ekspresi_reguler`:

`apt-file {{search|find}} --regexp {{ekspresi_reguler}}`
