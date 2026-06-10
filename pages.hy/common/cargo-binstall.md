# բեռների աղբարկղ

> Տեղադրեք Rust երկուականներ CI արտեֆակտներից:.
> Ընկնում է `cargo install`-ի (սկզբնական կոդից), եթե երկուականներ չկան:.
> Նշում. սա ներկառուցված Cargo հրաման չէ, նախ պետք է այն տեղադրել:.
> Լրացուցիչ տեղեկություններ. <https://github.com/cargo-bins/cargo-binstall>:.

- Տեղադրեք փաթեթ <https://crates.io>-ից.:

`cargo binstall {{package}}`

- Տեղադրեք փաթեթի որոշակի տարբերակ (վերջին լռելյայն).:

`cargo binstall {{package}}@{{version}}`

- Տեղադրեք փաթեթ և անջատեք հաստատման հուշումները.:

`cargo binstall {{[-y|--no-confirm]}} {{package}}`
