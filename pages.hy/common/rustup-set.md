# rustup հավաքածու

> Փոխել `rustup` կարգավորումները:.
> Լրացուցիչ տեղեկություններ. <https://rust-lang.github.io/rustup/>:.

- Սահմանեք լռելյայն հոսթ եռակի.:

`rustup set default-host {{host_triple}}`

- Սահմանեք լռելյայն պրոֆիլը (`minimal`-ը ներառում է միայն `rustc`, `rust-std` և `cargo`, մինչդեռ `default` ավելացնում է `rust-docs`, `rustfmt`LINE_, `rustfmt`__, և:

`rustup set profile {{minimal|default}}`

- Սահմանեք, արդյոք `rustup`-ը պետք է թարմացվի `rustup update`-ն աշխատեցնելիս:

`rustup set auto-self-update {{enable|disable|check-only}}`
