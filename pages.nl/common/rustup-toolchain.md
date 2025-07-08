# rustup toolchain

> Beheer Rust toolchains.
> Bekijk `rustup help toolchain` voor meer informatie over toolchains.
> Meer informatie: <https://rust-lang.github.io/rustup>.

- Installeer of update een bepaalde toolchain:

`rustup toolchain install {{toolchain}}`

- Deïnstalleer een toolchain:

`rustup toolchain uninstall {{toolchain}}`

- Toon geïnstalleerde toolchains:

`rustup toolchain list`

- Maak een aangepaste toolchain door te symlinken naar een map:

`rustup toolchain link {{aangepaste_toolchain_naam}} {{pad/naar/map}}`
