# բեռների ավելացում

> Ավելացրեք կախվածություններ Rust նախագծի `Cargo.toml` մանիֆեստում:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/cargo-add.html>:.

- Ավելացրեք կախվածության վերջին տարբերակը ընթացիկ նախագծին.:

`cargo add {{dependency}}`

- Ավելացնել կախվածության հատուկ տարբերակ.:

`cargo add {{dependency}}@{{version}}`

- Ավելացրեք կախվածություն և միացրեք մեկ կամ մի քանի հատուկ առանձնահատկություններ.:

`cargo add {{dependency}} {{[-F|--features]}} {{feature_1,feature_2,...}}`

- Ավելացրեք կամընտիր կախվածություն, որն այնուհետև բացահայտվում է որպես տուփի հատկանիշ.:

`cargo add {{dependency}} --optional`

- Ավելացրեք տեղական արկղ որպես կախվածություն.:

`cargo add --path {{path/to/crate_directory}}`

- Ավելացրեք զարգացում կամ ստեղծեք կախվածություն.:

`cargo add {{dependency}} --{{dev|build}}`

- Ավելացրեք կախվածություն բոլոր լռելյայն հնարավորություններով անջատված.:

`cargo add {{dependency}} --no-default-features`
