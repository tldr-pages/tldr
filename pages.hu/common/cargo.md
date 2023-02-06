# cargo

> A Rust projektek és modulfüggőségeik (crates) kezelése. Néhány alparancsnak, mint például a `cargo build`, saját használati dokumentációja van. További információ: <https://crates.io>.

- Ládák keresése:

`cargo search {{search_string}}`

- Crate telepítése:

`cargo install {{crate_name}}`

- Telepített crates listázása:

`cargo install --list`

- Új bináris vagy könyvtári Rust projekt létrehozása az aktuális könyvtárban:

`cargo init --{{bin|lib}}`

- Új bináris vagy könyvtári Rust projekt létrehozása a megadott könyvtárban:

`cargo new {{path/to/directory}} --{{bin|lib}}`

- Rust projekt építése az aktuális könyvtárban:

`cargo build`

- A rust projekt építése az aktuális könyvtárban az éjszakai fordítóval:

`cargo +nightly build`

- Építés meghatározott számú szál felhasználásával (alapértelmezett a CPU-magok száma):

`cargo build --jobs {{number_of_threads}}`
