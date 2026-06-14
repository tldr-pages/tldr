# բեռնափոխադրում

> Ստեղծեք Debian փաթեթներ Cargo նախագծերից:.
> Նշում. սա ներկառուցված Cargo հրաման չէ, նախ պետք է այն տեղադրել:.
> Լրացուցիչ տեղեկություններ. <https://github.com/kornelski/cargo-deb>:.

- Ստեղծեք Debian փաթեթ նախագծից.:

`cargo deb`

- Գրեք `.deb` ֆայլը նշված ֆայլում կամ գրացուցակում.:

`cargo deb {{[-o|--output]}} {{path/to/file_or_directory}}`

- Կազմել նշված Rust թիրախ եռակի համար.:

`cargo deb --target {{x86_64-unknown-linux-gnu}}`

- Ընտրեք, թե որ փաթեթն օգտագործել բեռների աշխատանքային տարածքում.:

`cargo deb {{[-p|--package]}} {{package_name}}`

- Անմիջապես տեղադրեք ստեղծված փաթեթը.:

`cargo deb --install`
