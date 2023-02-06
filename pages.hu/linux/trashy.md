# trashy

> A `rm` és a `trash-cli` alternatívája, Rust nyelven írva. További információ: <https://github.com/oberblastmeister/trashy>.

- Egy adott fájl áthelyezése a szemétbe:

`trash {{path/to/file}}`

- Konkrét fájlok áthelyezése a szemetesbe:

`trash {{path/to/file1 path/to/file2 ...}}`

- A szemétben lévő elemek listázása:

`trash list`

- Egy adott fájl visszaállítása a szemetesből:

`trash restore {{file}}`

- Egy adott fájl eltávolítása a szemetesből:

`trash empty {{file}}`

- Az összes fájl visszaállítása a szemetesből:

`trash restore --all`

- Az összes fájl eltávolítása a szemetesből:

`trash empty --all`
