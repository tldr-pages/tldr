# rustc

> A Rust fordító. Feldolgozza, lefordítja és összekapcsolja a Rust nyelv forrásfájljait. További információ: <https://doc.rust-lang.org/rustc>.

- Egyetlen fájl fordítása:

`rustc {{path/to/file.rs}}`

- Kompilálás nagyfokú optimalizálással:

`rustc -O {{path/to/file.rs}}`

- Fordítás hibakeresési információkkal:

`rustc -g {{path/to/file.rs}}`

- Kompilálás az aktuális CPU-ra vonatkozó architektúra-specifikus optimalizációkkal:

`rustc -C target-cpu=native {{path/to/file.rs}}`

- Az aktuális CPU architektúra-specifikus optimalizációinak megjelenítése:

`rustc -C target-cpu=native --print cfg`

- Céllista megjelenítése:

`rustc --print target-list`

- Kompilálás egy adott célpontra:

`rustc --target {{target_triple}} {{path/to/file.rs}}`
