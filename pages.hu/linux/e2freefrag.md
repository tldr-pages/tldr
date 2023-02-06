# e2freefrag

> Az ext2/ext3/ext4 fájlrendszerek szabad hely töredezettségi információinak nyomtatása. További információ: <https://manned.org/e2freefrag>.

- Ellenőrizze, hogy hány szabad blokk van jelen összefüggő és igazított szabad területként:

`e2freefrag {{/dev/sdXN}}`

- Adja meg a darabméretet kilobájtban, hogy kiírja, hány szabad darab áll rendelkezésre:

`e2freefrag -c {{chunk_size_in_kb}} {{/dev/sdXN}}`
