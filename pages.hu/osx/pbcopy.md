# pbcopy

> Az adatok másolása a `stdin` oldalról a vágólapra. További információ: <https://ss64.com/osx/pbcopy.html>.

- Egy adott fájl tartalmának a vágólapra helyezése:

`pbcopy < {{path/to/file}}`

- Egy adott parancs eredményeinek a vágólapra helyezése:

`find . -type t -name "*.png" | pbcopy`
