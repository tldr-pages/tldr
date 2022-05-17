# gcc

> Praproses dan kompilasi kode sumber C dan C++, lalu rakit dan gabungkan bersama-sama.
> Informasi lebih lanjut: <https://gcc.gnu.org>.

- Mengubah beberapa sumber kode menjadi program:

`gcc {{sumber1.c}} {{sumber2.c}} --output {{program}}`

- Mengizinkan peringatan dan simbol debug di output:

`gcc {{sumber.c}} -Wall -Og --output {{program}}`

- Menyertakan pustaka dari direktori yang berbeda:

`gcc {{sumber.c}} --output {{program}} -I{{jalur_header}} -L{{jalur_pustaka}} -l{{nama_pustaka}}`

- Mengkompilasi kode sumber ke dalam bahasa tingkat rendah (assembly):

`gcc -S {{sumber.c}}`

- Mengkompilasi kode sumber tanpa digabungkan:

`gcc -c {{sumber.c}}`
