# clang++

> Susun kode C++.
> Part of LLVM.
> Informasi lebih lanjut: <https://clang.llvm.org/>.

- Ubah suatu berkas kode sumber menjadi program:

`clang++ {{jalan/menuju/sumber1.c jalan/menuju/sumber2.cpp ...}} {{-o|--output}} {{jalan/menuju/program}}`

- Tampilkan pesan peringatan dan galat dalam [o]utput:

`clang++ {{jalan/menuju/sumber.c}} -Wall {{-o|--output}} {{jalan/menuju/program}}`

- Izinkan peringatan dan simbol debug dalam [o]utput:

`clang++ {{jalan/menuju/sumber.c}} -Wall {{-g|--debug}} -Og {{-o|--output}} {{jalan/menuju/program}}`

- Pilih standar bahasa untuk dikompilasi:

`clang++ {{path/to/source.cpp}} -std={{c++20}} {{-o|--output}} {{path/to/output_executable}}`

- Sertakan pustaka (library) dari direktori yang berbeda:

`clang++ {{jalan/menuju/sumber.c}} {{-o|--output}} {{jalan/menuju/program}} -I{{jalan/menuju/header}} -L{{jalan/menuju/pustaka}} -l{{nama_pustaka}}`

- Susun kode sumber menjadi program dalam format LLVM Intermediate Representation (IR):

`clang++ {{-S|--assemble}} -emit-llvm {{jalan/menuju/sumber.c}} {{-o|--output}} {{jalan/menuju/program.ll}}`

- [O]ptimalkan progam yang disusun agar dapat dijalankan lebih cepat:

`clang++ {{path/to/source.c}} -O{{1|2|3|fast}} {{-o|--output}} {{path/to/output_executable}}`
