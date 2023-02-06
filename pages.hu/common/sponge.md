# sponge

> A kimeneti fájl írása előtt felszívja a bemenetet. További információ: <https://manned.org/sponge>.

- A fájl tartalmának hozzáadása a forrásfájlhoz:

`cat {{path/to/file}} | sponge -a {{path/to/file}}`

- Eltávolítja az összes #-vel kezdődő sort egy fájlban:

`grep -v '^{{#}}' {{path/to/file}} | sponge {{path/to/file}}`
