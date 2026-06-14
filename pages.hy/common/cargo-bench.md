# բեռների նստարան

> Կազմել և կատարել հենանիշեր:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/cargo-bench.html>:.

- Կատարել փաթեթի բոլոր չափանիշները.:

`cargo bench`

- Մի կանգնեք, երբ չափանիշը ձախողվում է.:

`cargo bench --no-fail-fast`

- Կազմեք, բայց մի գործարկեք հենանիշեր.:

`cargo bench --no-run`

- Հենանիշ նշեք նշված հենանիշը.:

`cargo bench --bench {{benchmark}}`

- Հենանիշ տվյալ պրոֆիլով (կանխադրված՝ `bench`):

`cargo bench --profile {{profile}}`

- Հենանիշային բոլոր օրինակային թիրախները.:

`cargo bench --examples`

- Հենանիշային բոլոր երկուական թիրախները.:

`cargo bench --bins`

- Հենանիշային փաթեթի գրադարանը.:

`cargo bench --lib`
