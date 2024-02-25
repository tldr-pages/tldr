# apt-file

> Mencari file-file di dalam paket `apt`, termasuk yang belum diinstal.
> Informasi lebih lanjut: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- Memperbarui basis data metadata:

`sudo apt update`

- Mencari paket yang berisi nama file atau path yang diinputkan:

`apt-file {{search|find}} {{partial_path/to/file}}`

- Menampilkan daftar konten dari sebuah paket:

`apt-file {{show|list}} {{package}}`

- Mencari paket yang yang sesuai dengan `regular_expression`:

`apt-file {{search|find}} --regexp {{regular_expression}}`
