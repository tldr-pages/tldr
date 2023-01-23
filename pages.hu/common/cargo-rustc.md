# cargo rustc

> Rust csomag fordítása, és extra opciók átadása a fordítónak. További információ: <https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- A `Cargo.toml` manifeszt fájlban meghatározott csomag vagy csomagok összeállítása az aktuális munkakönyvtárban:

`cargo rustc`

- Építsen artefaktumokat kiadási módban, optimalizációkkal:

`cargo rustc --release`

- Fordítás az aktuális CPU-ra vonatkozó architektúra-specifikus optimalizációkkal:

`cargo rustc --release -- -C target-cpu=native`

- Fordítás sebességoptimalizálással:

`cargo rustc -- -C opt-level {{1|2|3}}`

- Fordítás \[s\]ize optimalizálással (`z` kikapcsolja a ciklusvektorizálást is):

`cargo rustc -- -C opt-level {{s|z}}`

- Ellenőrizze, hogy a csomagja nem biztonságos kódot használ-e:

`cargo rustc --lib -- -D unsafe-code`

- Egy adott csomag összeállítása:

`cargo rustc --package {{package}}`

- Csak a megadott bináris csomagot építse:

`cargo --bin {{name}}`
