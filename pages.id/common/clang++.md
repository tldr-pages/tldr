# clang++

> Susun kode C++.
> Part of LLVM.
> Informasi lebih lanjut: <https://clang.llvm.org/docs/UsersManual.html#command-line-options>.

- Ubah suatu berkas kode sumber menjadi program:

`clang++ {{jalan/menuju/sumber1.cpp jalan/menuju/sumber2.cpp ...}} {{[-o|--output]}} {{jalan/menuju/program}}`

- Tampilkan pesan peringatan dan galat dalam output:

`clang++ {{jalan/menuju/sumber.cpp}} -Wall {{[-o|--output]}} {{jalan/menuju/program}}`

- Izinkan peringatan dan simbol debug dalam output:

`clang++ {{jalan/menuju/sumber.cpp}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{jalan/menuju/program}}`

- Pilih standar bahasa untuk dikompilasi:

`clang++ {{jalan/menuju/sumber.cpp}} -std={{c++20}} {{[-o|--output]}} {{jalan/menuju/program}}`

- Sertakan pustaka (library) dari direktori yang berbeda:

`clang++ {{jalan/menuju/sumber.cpp}} {{[-o|--output]}} {{jalan/menuju/program}} -I{{jalan/menuju/header}} -L{{jalan/menuju/pustaka}} -l{{nama_pustaka}}`

- Susun kode sumber menjadi program dalam format LLVM Intermediate Representation (IR):

`clang++ {{[-S|--assemble]}} -emit-llvm {{jalan/menuju/sumber.cpp}} {{[-o|--output]}} {{jalan/menuju/program.ll}}`

- [O]ptimalkan progam yang disusun agar dapat dijalankan lebih cepat:

`clang++ {{jalan/menuju/sumber.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{jalan/menuju/program}}`

- Tampilkan versi penyusun:

`clang++ --version`
