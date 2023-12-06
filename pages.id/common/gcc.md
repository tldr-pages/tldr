# gcc

> Praproses dan susun kode sumber C dan C++, lalu rakit dan gabungkan bersama-sama.
> Informasi lebih lanjut: <https://gcc.gnu.org>.

- Ubah beberapa sumber kode menjadi program:

`gcc {{jalan/menuju/sumber1.c jalan/menuju/sumber2.c ...}} -o {{jalan/menuju/program}}`

- Izinkan peringatan dan simbol debug dalam [o]utput:

`gcc {{jalan/menuju/sumber.c}} -Wall -g -Og -o {{jalan/menuju/program}}`

- Sertakan pustaka (library) dari direktori yang berbeda:

`gcc {{sumber.c}} -o {{jalan/menuju/program}} -I{{jalan/menuju/header}} -L{{jalan/menuju/pustaka}} -l{{nama_pustaka}}`

- Susun kode sumber ke dalam bahasa tingkat rendah (assembly):

`gcc -S {{jalan/menuju/sumber.c}}`

- Susun kode sumber tanpa digabungkan:

`gcc -c {{jalan/menuju/sumber.c}}`

- [O]ptimalkan progam yang disusun agar dapat dijalankan lebih cepat:

`gcc {{path/to/source.c}} -O{{1|2|3|fast}} -o {{path/to/output_executable}}`
