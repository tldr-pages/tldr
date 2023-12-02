# gcc

> Praproses dan susun kode sumber C dan C++, lalu rakit dan gabungkan bersama-sama.
> Informasi lebih lanjut: <https://gcc.gnu.org>.

- Ubah beberapa sumber kode menjadi program:

`gcc {{sumber1.c}} {{sumber2.c}} --output {{program}}`

- Izinkan peringatan dan simbol debug dalam output:

`gcc {{sumber.c}} -Wall -Og --output {{program}}`

- Sertakan pustaka (library) dari direktori yang berbeda:

`gcc {{sumber.c}} --output {{program}} -I{{jalur_header}} -L{{jalur_pustaka}} -l{{nama_pustaka}}`

- Susun kode sumber ke dalam bahasa tingkat rendah (assembly):

`gcc -S {{sumber.c}}`

- Susun kode sumber tanpa digabungkan:

`gcc -c {{sumber.c}}`
