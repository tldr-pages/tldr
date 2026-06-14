# rustdoc

> Ստեղծեք փաստաթղթեր Rust crate-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/stable/rustdoc/>:.

- Ստեղծեք փաստաթղթեր արկղի արմատից.:

`rustdoc {{src/lib.rs}}`

- Անվանեք նախագծի համար.:

`rustdoc {{src/lib.rs}} --crate-name {{name}}`

- Ստեղծեք փաստաթղթեր Markdown ֆայլերից.:

`rustdoc {{path/to/file.md}}`

- Նշեք ելքային գրացուցակը.:

`rustdoc {{src/lib.rs}} {{[-o|--out-dir]}} {{path/to/output_directory}}`

- Ցուցադրել օգնությունը.:

`rustdoc {{[-h|--help]}}`
