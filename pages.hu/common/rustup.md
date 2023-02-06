# rustup

> Rust toolchain telepítő. Rust toolchains telepítése, kezelése és frissítése. További információ: <https://github.com/rust-lang/rustup.rs>.

- Telepítse a rendszeréhez tartozó éjszakai toolchaint:

`rustup install nightly`

- Váltson át az alapértelmezett toolchaint nightlyre, hogy a `cargo` és a `rustc` parancsok azt használják:

`rustup default nightly`

- Használja a nightly toolchaint, amikor az aktuális projekten belül van, de a globális beállításokat hagyja változatlanul:

`rustup override set nightly`

- Frissítse az összes toolchaint:

`rustup update`

- A telepített toolchains listázása:

`rustup show`

- A cargo build futtatása egy bizonyos toolchainnel:

`rustup run {{toolchain_name}} cargo build`

- A helyi rust dokumentáció megnyitása az alapértelmezett webböngészőben:

`rustup doc`
