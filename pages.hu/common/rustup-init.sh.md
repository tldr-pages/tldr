# rustup-init.sh

> Szkript a `rustup` és a Rust toolchain telepítéséhez. További információ: <https://forge.rust-lang.org/infra/other-installation-methods.html#rustup>.

- Töltse le és futtassa a `rustup-init` a `rustup` és az alapértelmezett Rust toolchain telepítéséhez:

`curl https://sh.rustup.rs -sSf | sh -s`

- Töltse le és futtassa a `rustup-init`, és adjon át neki argumentumokat:

`curl https://sh.rustup.rs -sSf | sh -s -- {{arguments}}`

- Futtassa a `rustup-init` és adja meg a telepítendő további komponenseket vagy célokat:

`rustup-init.sh --target {{target}} --component {{component}}`

- Futtassa a `rustup-init` és adja meg a telepítendő alapértelmezett toolchaint:

`rustup-init.sh --default-toolchain {{toolchain}}`

- A `rustup-init` futtatása és semmilyen toolchain telepítése:

`rustup-init.sh --default-toolchain {{none}}`

- A `rustup-init` futtatása és egy telepítési profil megadása:

`rustup-init.sh --profile {{minimal|default|complete}}`

- A `rustup-init` futtatása megerősítés kérése nélkül:

`rustup-init.sh -y`
