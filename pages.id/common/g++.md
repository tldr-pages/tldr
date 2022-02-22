# g++

> Kompilasi sumber kode C++.
> Bagian dari GCC (GNU Compiler Collection).
> Informasi lebih lanjut: <https://gcc.gnu.org>.

- Mengubah berkas sumber kode menjadi program:

`g++ {{sumber.cpp}} -o {{program}}`

- Menampilkan (hampir) semua kesalahan dan peringatan:

`g++ {{sumber.cpp}} -Wall -o {{program}}`

- Memilih standar bahasa untuk dikompilasi (C++98/C++11/C++14/C++17):

`g++ {{sumber.cpp}} -std={{standar_bahasa}} -o {{program}}`

- Menyertakan pustaka di direktori yang berbeda:

`g++ {{sumber.cpp}} -o {{program}} -I{{jalur_header}} -L{{jalur_pustaka}} -l{{nama_pustaka}}`
