# բեռների թարմացում

> Թարմացրեք կախվածությունները, ինչպես գրանցված է `Cargo.lock`-ում:.
> Լրացուցիչ տեղեկություններ. <https://doc.rust-lang.org/cargo/commands/cargo-update.html>:.

- Թարմացրեք կախվածությունները `Cargo.lock`-ում վերջին հնարավոր տարբերակին.:

`cargo update`

- Ցուցադրեք այն, ինչ կթարմացվի, բայց իրականում մի գրեք կողպեքի ֆայլը.:

`cargo update {{[-n|--dry-run]}}`

- Թարմացրեք միայն նշված կախվածությունները.:

`cargo update --package {{dependency1}} --package {{dependency2}} --package {{dependency3}}`

- Սահմանեք որոշակի կախվածություն որոշակի տարբերակի համար.:

`cargo update --package {{dependency}} --precise {{1.2.3}}`
