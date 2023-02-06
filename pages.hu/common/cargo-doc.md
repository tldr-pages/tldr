# cargo doc

> A Rust csomagok dokumentációjának összeállítása és megtekintése offline. További információ: <https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- Az alapértelmezett csomagdokumentáció összeállítása és megtekintése a böngészőben:

`cargo doc --open`

- Dokumentáció készítése hálózati hozzáférés nélkül:

`cargo doc --offline`

- Egy adott csomag dokumentációjának megtekintése:

`cargo doc --open --package {{package}}`

- Egy adott csomag dokumentációjának offline megtekintése:

`cargo doc --open --offline --package {{package}}`
