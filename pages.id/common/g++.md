# g++

> Susun kode sumber C++.
> Bagian dari GCC (GNU Compiler Collection).
> Informasi lebih lanjut: <https://gcc.gnu.org/onlinedocs/gcc/C_002b_002b-Dialect-Options.html>.

- Ubah suatu berkas kode sumber menjadi program:

`g++ {{jalan/menuju/sumber1.c jalan/menuju/sumber2.cpp ...}} {{[-o|--output]}} {{jalan/menuju/program}}`

- Tampilkan pesan peringatan dan galat dalam output:

`g++ {{jalan/menuju/sumber.cpp}} -Wall {{[-o|--output]}} {{jalan/menuju/program}}`

- Izinkan peringatan dan simbol debug dalam output:

`g++ {{jalan/menuju/sumber.cpp}} -Wall {{-g|--debug}} -Og {{[-o|--output]}} {{jalan/menuju/program}}`

- Pilih standar bahasa untuk dikompilasi (C++98/C++11/C++14/C++17):

`g++ {{jalan/menuju/sumber.cpp}} -std={{c++98|c++11|c++14|c++17}} {{[-o|--output]}} {{jalan/menuju/program}}`

- Sertakan pustaka (library) dari direktori yang berbeda:

`g++ {{jalan/menuju/sumber.cpp}} {{[-o|--output]}} {{jalan/menuju/program}} -I{{jalan/menuju/header}} -L{{jalan/menuju/pustaka}} -l{{nama_pustaka}}`

- Susun dan gabungkan beberapa berkas kode sumber menjadi suatu berkas program biner:

`g++ {{-c|--compile}} {{jalan/menuju/sumber1.cpp jalan/menuju/sumber2.cpp ...}} && g++ {{[-o|--output]}} {{jalan/menuju/program}} {{jalan/menuju/sumber1.o jalan/menuju/sumber2.o ...}}`

- [O]ptimalkan progam yang disusun agar dapat dijalankan lebih cepat:

`g++ {{jalan/menuju/sumber.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{jalan/menuju/program}}`

- Tampilkan versi penyusun:

`g++ --version`
