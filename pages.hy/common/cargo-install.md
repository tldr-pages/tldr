# բեռների տեղադրում

> Կառուցեք և տեղադրեք Rust երկուական տարբերակ:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/cargo-install.html>:.

- Տեղադրեք փաթեթ <https://crates.io>-ից (տարբերակը կամընտիր է, լռելյայն վերջինը).:

`cargo install {{package}}@{{version}}`

- Տեղադրեք փաթեթ նշված Git պահոցից.:

`cargo install --git {{repo_url}}`

- Կառուցեք նշված ճյուղից/պիտակից/կոմիտից Git պահոցից տեղադրելիս.:

`cargo install --git {{repo_url}} --{{branch|tag|rev}} {{branch_name|tag|commit_hash}}`

- Տեղադրեք փաթեթ տեղական գրացուցակից.:

`cargo install --path {{path/to/package}}`

- Թվարկեք բոլոր տեղադրված փաթեթները և դրանց տարբերակները.:

`cargo install --list`
