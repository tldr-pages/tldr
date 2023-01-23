# cut

> Mezők kivágása a `stdin` vagy fájlokból. További információ: <https://www.gnu.org/software/coreutils/cut>.

- Az egyes sorok egy adott karakter/mező tartományának kinyomtatása:

`{{command}} | cut --{{characters|fields}}={{1|1,10|1-10|1-|-10}}`

- Az egyes sorok egy meghatározott elhatárolójelekkel ellátott tartományának nyomtatása:

`{{command}} | cut --delimiter="{{,}}" --{{fields}}={{1}}`

- Az adott fájl minden egyes sorának tartományának nyomtatása:

`cut --{{characters}}={{1}} {{path/to/file}}`
