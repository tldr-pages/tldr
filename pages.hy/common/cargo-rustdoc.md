# բեռների rustdoc

> Կառուցեք Rust փաթեթների փաստաթղթերը:.
> Նման է `cargo doc`-ին, բայց կարող եք տարբերակներ փոխանցել `rustdoc`-ին: Տես `rustdoc --help` բոլոր հասանելի տարբերակները:.
> Տես նաև՝ `rustdoc`:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>:.

- Փոխանցեք ընտրանքները `rustdoc`-ին:

`cargo rustdoc -- {{rustdoc_options}}`

- Զգուշացրեք փաստաթղթային ծածկույթի մասին.:

`cargo rustdoc -- {{[-W|--warn]}} rustdoc::{{lint_name}}`

- Անտեսեք փաստաթղթային ծածկույթը.:

`cargo rustdoc -- {{[-A|--allow]}} rustdoc::{{lint_name}}`

- Փաստաթղթավորեք փաթեթի գրադարանը.:

`cargo rustdoc --lib`

- Փաստաթղթավորեք նշված երկուականը.:

`cargo rustdoc --bin {{name}}`

- Փաստաթղթավորեք նշված օրինակը.:

`cargo rustdoc --example {{name}}`

- Փաստաթղթավորեք նշված ինտեգրման թեստը.:

`cargo rustdoc --test {{name}}`
