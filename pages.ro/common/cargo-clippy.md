# cargo clippy

> O colecție de scame pentru a prinde greșelile obișnuite și pentru a îmbunătăți codul Rust.
> Mai multe informaţii: <https://github.com/rust-lang/rust-clippy>

- Rulați verificări peste codul din directorul curent:

`cargo clippy`

- Necesită ca `Cargo.lock` să fie la zi:

`cargo clippy --locked`

- Rulați verificări pe toate pachetele din spațiul de lucru:

`cargo clippy --workspace`

- Executați verificările pentru un pachet:

`cargo clippy --package {{package}}`

- Tratează avertismentele ca erori:

`RUSTFLAGS="-Dwarnings" cargo clippy -- -D warnings`

- Rulați verificări și ignorați avertismentele:

`cargo clippy -- -A warnings`

- Aplicați sugestia Clippy automat (experimentală și acceptată numai pe canalul de noapte):

`cargo clippy --fix -Z unstable-options`
