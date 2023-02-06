# ocamlc

> Az OCaml bájtkód fordító. Az OCaml értelmezővel futtatható futtatható állományokat készít. További információ: <https://ocaml.org>.

- Bináris állomány létrehozása egy forrásfájlból:

`ocamlc {{path/to/source_file.ml}}`

- Nevezett bináris állomány létrehozása egy forrásfájlból:

`ocamlc -o {{path/to/binary}} {{path/to/source_file.ml}}`

- Automatikusan generál egy modul aláírás (interfész) fájlt:

`ocamlc -i {{path/to/source_file.ml}}`
