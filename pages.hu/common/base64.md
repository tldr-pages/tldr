# base64

> Fájl vagy szabványos bemenet kódolása vagy dekódolása Base64-be vagy Base64-ből, szabványos kimenetre. További információ: <https://www.gnu.org/software/coreutils/base64>.

- Egy fájl tartalmának base64 kódolása és az eredmény kiírása a `stdout` címre:

`base64 {{path/to/file}}`

- Dekódolja egy fájl base64 tartalmát, és írja az eredményt a `stdout` címre:

`base64 --decode {{path/to/file}}`

- Enkódolás a `stdin`:

`{{somecommand}} | base64`

- Dekódolás a `stdin`:

`{{somecommand}} | base64 --decode`
