# բեռի հաշվետվություն

> Ցուցադրել տարբեր տեսակի հաշվետվություններ:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/cargo-report.html>:.

- Ցուցադրեք արկղերի հաշվետվություն, որն ի վերջո կդադարեցնի կազմելը.:

`cargo report future-incompatibilities`

- Ցուցադրել հաշվետվություն նշված բեռի կողմից ստեղծված ID-ով.:

`cargo report future-incompatibilities --id {{id}}`

- Ցուցադրել հաշվետվություն նշված փաթեթի համար.:

`cargo report future-incompatibilities {{[-p|--package]}} {{package}}`
