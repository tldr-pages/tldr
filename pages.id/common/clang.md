# clang

> Susun kode sumber C, C++, dan Objective-C. Dapat dipakai sebagai pengganti mutlak (drop-in) bagi GCC.
> Part of LLVM.
> Informasi lebih lanjut: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Ubah suatu berkas kode sumber menjadi program:

`clang {{jalan/menuju/sumber1.c jalan/menuju/sumber2.c ...}} {{[-o|--output]}} {{jalan/menuju/program}}`

- Tampilkan pesan peringatan dan galat dalam output:

`clang {{jalan/menuju/sumber.c}} -Wall {{[-o|--output]}} {{jalan/menuju/program}}`

- Izinkan peringatan dan simbol debug dalam output:

`clang {{jalan/menuju/sumber.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{jalan/menuju/program}}`

- Sertakan pustaka (library) dari direktori yang berbeda:

`clang {{jalan/menuju/sumber.c}} {{[-o|--output]}} {{jalan/menuju/program}} -I{{jalan/menuju/header}} -L{{jalan/menuju/pustaka}} -l{{nama_pustaka}}`

- Susun kode sumber menjadi program dalam format LLVM Intermediate Representation (IR):

`clang {{[-S|--assemble]}} -emit-llvm {{jalan/menuju/sumber.c}} {{[-o|--output]}} {{jalan/menuju/program.ll}}`

- Susun kode sumber tanpa digabungkan:

`clang {{[-c|--compile]}} {{jalan/menuju/sumber.c}}`

- [O]ptimalkan progam yang disusun agar dapat dijalankan lebih cepat:

`clang {{jalan/menuju/sumber.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{jalan/menuju/program}}`

- Tampilkan versi penyusun:

`clang --version`
