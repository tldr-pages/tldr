# rustfmt

> Eszköz a Rust forráskód formázására. További információ: <https://github.com/rust-lang/rustfmt>.

- Formázzon egy fájlt, helyben felülírva az eredeti fájlt:

`rustfmt {{path/to/source.rs}}`

- Egy fájl ellenőrzése formázás szempontjából, és a változások megjelenítése a konzolon:

`rustfmt --check {{path/to/source.rs}}`

- Biztonsági mentés a formázás előtt módosított fájlokról (az eredeti fájl átnevezése `.bk` kiterjesztéssel):

`rustfmt --backup {{path/to/source.rs}}`
