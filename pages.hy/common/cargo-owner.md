# բեռների սեփականատեր

> Կառավարեք ռեեստրի արկղի սեփականատերերին:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/cargo-owner.html>:.

- Հրավիրեք տվյալ օգտվողին կամ թիմին որպես սեփականատեր.:

`cargo owner {{[-a|--add]}} {{username|github:org_name:team_name}} {{crate}}`

- Հեռացրեք տվյալ օգտվողին կամ թիմին որպես սեփականատեր.:

`cargo owner {{[-r|--remove]}} {{username|github:org_name:team_name}} {{crate}}`

- Նշեք տուփի սեփականատերերին.:

`cargo owner {{[-l|--list]}} {{crate}}`

- Օգտագործեք նշված ռեեստրը (ռեգիստրի անունները կարող են սահմանվել կազմաձևում - լռելյայն է <https://crates.io>):

`cargo owner --registry {{name}}`
