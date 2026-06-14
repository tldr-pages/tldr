# բեռների տեղորոշում-նախագիծ

> Տպեք նախագծի `Cargo.toml` մանիֆեստի ամբողջական ուղին:.
> Եթե նախագիծը աշխատանքային տարածքի մաս է, ապա ցուցադրվում է նախագծի մանիֆեստը, այլ ոչ թե աշխատանքային տարածքը:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/cargo-locate-project.html>:.

- Ցուցադրել JSON օբյեկտը `Cargo.toml` մանիֆեստի ամբողջական ուղով.:

`cargo locate-project`

- Ցուցադրել նախագծի ուղին նշված ձևաչափով.:

`cargo locate-project --message-format {{plain|json}}`

- Ցուցադրել `Cargo.toml` մանիֆեստը, որը գտնվում է աշխատանքային տարածքի արմատում՝ ի տարբերություն ընթացիկ աշխատանքային տարածքի անդամի.:

`cargo locate-project --workspace`

- Ցուցադրել որոշակի գրացուցակի `Cargo.toml` մանիֆեստը՝:

`cargo locate-project --manifest-path {{path/to/Cargo.toml}}`
