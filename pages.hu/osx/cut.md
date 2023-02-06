# cut

> Mezők kivágása a `stdin` vagy fájlokból. További információ: <https://manned.org/man/freebsd-13.0/cut.1>.

- Az egyes sorok egy adott karakter/mező tartományának nyomtatása:

`{{command}} | cut -{{c|f}} {{1|1,10|1-10|1-|-10}}`

- Az egyes sorok egy adott elhatároló karakter- és karaktertartományának nyomtatása:

`{{command}} | cut -d "{{,}}" -{{c}} {{1}}`

- Egy adott fájl minden egyes sorának tartományának nyomtatása:

`cut -{{c}} {{1}} {{path/to/file}}`
