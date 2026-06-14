# rustup գործիքաշղթա

> Կառավարեք Rust գործիքների շղթաները:.
> Գործիքների շղթաների մասին լրացուցիչ տեղեկությունների համար տես `rustup help toolchain`:.
> Լրացուցիչ տեղեկություններ. <https://rust-lang.github.io/rustup/>:.

- Տեղադրեք կամ թարմացրեք տվյալ գործիքների շղթան.:

`rustup toolchain install {{toolchain}}`

- Տեղահանել գործիքների շղթան.:

`rustup toolchain uninstall {{toolchain}}`

- Տեղադրված գործիքների շղթաների ցանկ.:

`rustup toolchain list`

- Ստեղծեք հարմարեցված գործիքների շղթա՝ համակցելով գրացուցակին՝:

`rustup toolchain link {{custom_toolchain_name}} {{path/to/directory}}`
