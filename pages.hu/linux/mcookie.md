# mcookie

> 128 bites véletlenszerű hexadecimális számokat generál. További információ: <https://manned.org/mcookie>.

- Véletlen szám generálása:

`mcookie`

- Egy véletlen szám generálása, egy fájl tartalmát használva a véletlenszerűség magjaként:

`mcookie --file {{path/to/file}}`

- Véletlen szám generálása, a véletlenszerűség magjaként egy fájl meghatározott számú bájtját használva:

`mcookie --file {{path/to/file}} --max-size {{number_of_bytes}}`

- Nyomtassa ki a felhasznált véletlenszerűség részleteit, például az egyes források eredetét és magját:

`mcookie --verbose`
