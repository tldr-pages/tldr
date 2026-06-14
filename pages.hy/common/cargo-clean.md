# բեռների մաքուր

> Հեռացրեք ստեղծված արտեֆակտները `target` գրացուցակից:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/cargo-clean.html>:.

- Հեռացրեք `target` ամբողջ գրացուցակը.:

`cargo clean`

- Հեռացրեք փաստաթղթերի արտեֆակտները (`target/doc` գրացուցակը).:

`cargo clean --doc`

- Հեռացրեք թողարկման արտեֆակտները (`target/release` գրացուցակը).:

`cargo clean {{[-r|--release]}}`

- Հեռացրեք արտեֆակտները տվյալ պրոֆիլի գրացուցակում (այս դեպքում՝ `target/debug`):

`cargo clean --profile {{dev}}`
