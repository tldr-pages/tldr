# rustup բաղադրիչ

> Փոփոխել գործիքաշարի տեղադրված բաղադրիչները:.
> Առանց `--toolchain` ընտրանքի, `rustup`-ը կօգտագործի լռելյայն գործիքաշարը: Գործիքների շղթաների մասին լրացուցիչ տեղեկությունների համար տես `rustup help toolchain`:.
> Լրացուցիչ տեղեկություններ. <https://rust-lang.github.io/rustup/>:.

- Գործիքների շղթային բաղադրիչ ավելացրեք.:

`rustup component add --toolchain {{toolchain}} {{component}}`

- Հեռացրեք բաղադրիչը գործիքների շղթայից.:

`rustup component remove --toolchain {{toolchain}} {{component}}`

- Գործիքների շղթայի համար տեղադրված և հասանելի բաղադրիչների ցանկ.:

`rustup component list --toolchain {{toolchain}}`

- Ցուցակեք տեղադրված բաղադրիչները գործիքաշարի համար.:

`rustup component list --toolchain {{toolchain}} --installed`
