# g++

> Kompilasi sumber kode C++.
> Bagian dari GCC (GNU Compiler Collection).
> Informasi lebih lanjut: <https://gcc.gnu.org>.

- Mengubah berkas sumber kode menjadi program:

`g++ {{jalan/menuju/sumber.cpp}} -o {{jalan/menuju/program}}`

- Menampilkan (hampir) semua kesalahan dan peringatan:

`g++ {{jalan/menuju/sumber.cpp}} -Wall -o {{jalan/menuju/program}}`

- Memilih standar bahasa untuk dikompilasi (C++98/C++11/C++14/C++17):

`g++ {{jalan/menuju/sumber.cpp}} -std={{standar_bahasa}} -o {{jalan/menuju/program}}`

- Menyertakan pustaka di direktori yang berbeda:

`g++ {{jalan/menuju/sumber.cpp}} -o {{jalan/menuju/program}} -I{{jalur_header}} -L{{jalur_pustaka}} -l{{nama_pustaka}}`
