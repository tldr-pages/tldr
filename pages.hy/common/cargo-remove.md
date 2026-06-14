# բեռի հեռացում

> Հեռացրեք կախվածությունները Rust նախագծի `Cargo.toml` մանիֆեստից:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/cargo-remove.html>:.

- Հեռացրեք կախվածությունը ընթացիկ նախագծից.:

`cargo remove {{dependency}}`

- Հեռացնել զարգացումը կամ ստեղծել կախվածություն.:

`cargo remove --{{dev|build}} {{dependency}}`

- Հեռացրեք կախվածությունը տվյալ թիրախային հարթակից.:

`cargo remove --target {{target}} {{dependency}}`
