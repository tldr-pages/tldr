# wasm2c

> Conversia unui fișier din formatul binar WebaseMbly într-un fișier sursă C și antet.

- Conversia unui fișier într-un fișier sursă C și antet și afișați-l în consola:

`wasm2c {{file.wasm}}`

- Scrieți ieșirea într-un fișier dat (`file.h` devine generat suplimentar):

`wasm2c {{file.wasm}} -o {{file.c}}`
