# rustup թիրախ

> Փոփոխել գործիքաշարի աջակցվող թիրախները:.
> Առանց `--toolchain` ընտրանքի, `rustup`-ը կօգտագործի լռելյայն գործիքաշարը: Գործիքների շղթաների մասին լրացուցիչ տեղեկությունների համար տես `rustup help toolchain`:.
> Լրացուցիչ տեղեկություններ. <https://rust-lang.github.io/rustup/>:.

- Թիրախ ավելացրեք գործիքների շղթային.:

`rustup target add --toolchain {{toolchain}} {{target}}`

- Հեռացրեք թիրախը գործիքների շղթայից.:

`rustup target remove --toolchain {{toolchain}} {{target}}`

- Գործիքների շղթայի համար հասանելի և տեղադրված թիրախների ցուցակ.:

`rustup target list --toolchain {{toolchain}}`

- Նշեք տեղադրված թիրախները գործիքաշարի համար.:

`rustup target list --toolchain {{toolchain}} --installed`
