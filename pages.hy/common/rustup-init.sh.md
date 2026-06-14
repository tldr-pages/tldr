# rustup-init.sh

> `rustup`-ը և Rust գործիքների շղթան տեղադրելու սկրիպտ:.
> Լրացուցիչ տեղեկություններ. <https://forge.rust-lang.org/infra/other-installation-methods.html#rustup>:.

- Ներբեռնեք և գործարկեք `rustup-init`-ը՝ `rustup`-ը և Rust գործիքների լռելյայն շղթան տեղադրելու համար.:

`curl https://sh.rustup.rs {{[-sSf|--silent --show-error --fail]}} | sh -s`

- Ներբեռնեք և գործարկեք `rustup-init`-ը և փոխանցեք փաստարկներ դրան.:

`curl https://sh.rustup.rs {{[-sSf|--silent --show-error --fail]}} | sh -s -- {{arguments}}`

- Գործարկեք `rustup-init`-ը և տեղադրեք լրացուցիչ բաղադրիչներ կամ թիրախներ՝:

`rustup-init.sh --target {{target}} --component {{component}}`

- Գործարկեք `rustup-init`-ը և նշեք տեղադրման լռելյայն գործիքաշարը՝:

`rustup-init.sh --default-toolchain {{toolchain}}`

- Գործարկեք `rustup-init`-ը և մի տեղադրեք որևէ գործիքաշար.:

`rustup-init.sh --default-toolchain {{none}}`

- Գործարկեք `rustup-init`-ը և նշեք տեղադրման պրոֆիլը՝:

`rustup-init.sh --profile {{minimal|default|complete}}`

- Գործարկեք `rustup-init`-ը՝ առանց հաստատում խնդրելու.:

`rustup-init.sh -y`
