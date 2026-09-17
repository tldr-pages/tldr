# addr2line

> Konversi alamat dari file biner menjadi nama file dan nomor baris.
> Informasi lebih lanjut: <https://manned.org/addr2line>.

- Tampilkan nama file dan nomor baris dari source code berdasarkan alamat instruksi dalam sebuah file executable:

`addr2line {{[-e|--exe]}} {{path/ke/executable}} {{address}}`

- Tampilkan nama fungsi, nama file, dan nomor baris:

`addr2line {{[-e|--exe]}} {{path/ke/executable}} {{[-f|--functions]}} {{address}}`

- Lakukan demangle pada nama fungsi untuk kode C++:

`addr2line {{[-e|--exe]}} {{path/ke/executable}} {{[-f|--functions]}} {{[-C|--demangle]}} {{address}}`
