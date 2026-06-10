# բեռների ստուգում-նախագիծ

> Ստուգեք `Cargo.toml` մանիֆեստի ճիշտությունը և արդյունքը տպեք որպես JSON օբյեկտ:.
> Նշում. այս հրամանը հնացած է և ապագայում կարող է հեռացվել:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/deprecated-and-removed.html>:.

- Ստուգեք ընթացիկ նախագծի մանիֆեստի ճիշտությունը.:

`cargo verify-project`

- Ստուգեք նշված մանիֆեստի ֆայլի ճիշտությունը.:

`cargo verify-project --manifest-path {{path/to/Cargo.toml}}`
