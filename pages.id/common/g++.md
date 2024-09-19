# g++

> Susun kode sumber C++.
> Bagian dari GCC (GNU Compiler Collection).
> Informasi lebih lanjut: <https://gcc.gnu.org>.

- Ubah suatu berkas kode sumber menjadi program:

`g++ {{jalan/menuju/sumber1.c jalan/menuju/sumber2.cpp ...}} {{-o|--output}} {{jalan/menuju/program}}`

- Tampilkan pesan peringatan dan galat dalam [o]utput:

`g++ {{jalan/menuju/sumber.c}} -Wall {{-o|--output}} {{jalan/menuju/program}}`

- Izinkan peringatan dan simbol debug dalam [o]utput:

`g++ {{jalan/menuju/sumber.c}} -Wall {{-g|--debug}} -Og {{-o|--output}} {{jalan/menuju/program}}`

- Pilih standar bahasa untuk dikompilasi:

`g++ {{path/to/source.cpp}} -std={{c++20}} {{-o|--output}} {{path/to/output_executable}}`

- Sertakan pustaka (library) dari direktori yang berbeda:

`g++ {{jalan/menuju/sumber.c}} {{-o|--output}} {{jalan/menuju/program}} -I{{jalan/menuju/header}} -L{{jalan/menuju/pustaka}} -l{{nama_pustaka}}`

- Susun dan gabungkan beberapa berkas kode sumber menjadi suatu berkas program biner:

`g++ {{-c|--compile}} {{jalan/menuju/sumber1.cpp jalan/menuju/sumber2.cpp ...}} && g++ {{-o|--output}} {{jalan/menuju/program}} {{jalan/menuju/sumber1.o jalan/menuju/sumber2.o ...}}`

- [O]ptimalkan progam yang disusun agar dapat dijalankan lebih cepat:

`g++ {{path/to/source.c}} -O{{1|2|3|fast}} {{-o|--output}} {{path/to/output_executable}}`
