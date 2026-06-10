# բեռների փաթեթ

> Հավաքեք տեղական փաթեթը բաշխվող tarball-ի մեջ (`.crate` ֆայլ):.
> Նման է `cargo publish --dry-run`-ին, բայց ունի ավելի շատ տարբերակներ:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/cargo-package.html>:.

- Կատարեք ստուգումներ և ստեղծեք `.crate` ֆայլ (համարժեք `cargo publish --dry-run`):

`cargo package`

- Ցուցադրել, թե ինչ ֆայլեր կներառվեն tarball-ում առանց այն իրականում ստեղծելու.:

`cargo package {{[-l|--list]}}`
