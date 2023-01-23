# base32

> Fájl vagy szabványos bemenet kódolása vagy dekódolása Base32-be vagy Base32-ből, szabványos kimenetre. További információ: <https://www.gnu.org/software/coreutils/base32>.

- Egy fájl kódolása:

`base32 {{path/to/file}}`

- Fájl dekódolása:

`base32 --decode {{path/to/file}}`

- Enkódolás a `stdin` oldalról:

`{{somecommand}} | base32`

- Dekódolás a `stdin`:

`{{somecommand}} | base32 --decode`
