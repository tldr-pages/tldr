# բեռների ստուգում

> Ստուգեք տեղական փաթեթը և դրա բոլոր կախվածությունները սխալների համար:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/cargo-check.html>:.

- Ստուգեք ընթացիկ փաթեթը.:

`cargo {{[c|check]}}`

- Ստուգեք բոլոր թեստերը.:

`cargo {{[c|check]}} --tests`

- Ստուգեք ինտեգրման թեստերը `tests/integration_test1.rs`-ում.:

`cargo {{[c|check]}} --test {{integration_test1}}`

- Ստուգեք ընթացիկ փաթեթը `feature1` և `feature2` հատկանիշներով:

`cargo {{[c|check]}} {{[-F|--features]}} {{feature1,feature2}}`

- Ստուգեք ընթացիկ փաթեթը, եթե կանխադրված գործառույթներն անջատված են.:

`cargo {{[c|check]}} --no-default-features`
