# gcc

> Praproses dan susun kode sumber C dan C++, lalu rakit dan gabungkan bersama-sama.
> Bagian dari GCC (GNU Compiler Collection).
> Informasi lebih lanjut: <https://gcc.gnu.org/onlinedocs/gcc/>.

- Ubah beberapa sumber kode menjadi program:

`gcc {{jalan/menuju/sumber1.c jalan/menuju/sumber2.c ...}} {{[-o|--output]}} {{jalan/menuju/program}}`

- Tampilkan pesan peringatan dan galat dalam output:

`gcc {{jalan/menuju/sumber.c}} -Wall {{[-o|--output]}} {{jalan/menuju/program}}`

- Izinkan peringatan dan simbol debug dalam output:

`gcc {{jalan/menuju/sumber.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{jalan/menuju/program}}`

- Sertakan pustaka (library) dari direktori yang berbeda:

`gcc {{jalan/menuju/sumber.c}} {{[-o|--output]}} {{jalan/menuju/program}} -I{{jalan/menuju/header}} -L{{jalan/menuju/pustaka}} -l{{nama_pustaka}}`

- Susun kode sumber ke dalam bahasa tingkat rendah (assembly):

`gcc {{[-S|--assemble]}} {{jalan/menuju/sumber.c}}`

- Susun kode sumber tanpa digabungkan:

`gcc {{[-c|--compile]}} {{jalan/menuju/sumber.c}}`

- [O]ptimalkan progam yang disusun agar dapat dijalankan lebih cepat:

`gcc {{jalan/menuju/sumber.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{jalan/menuju/program}}`

- Tampilkan versi penyusun:

`gcc --version`
