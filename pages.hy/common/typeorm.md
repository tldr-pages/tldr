#typorm

> JavaScript ORM, որը կարող է աշխատել Node.js, բրաուզերի, Cordova, Ionic, React Native, NativeScript և Electron հարթակներում:.
> Լրացուցիչ տեղեկություններ. <https://typeorm.io/docs/advanced-topics/using-cli/#initialize-a-new-typeorm-project>:.

- Ստեղծեք նոր սկզբնական TypeORM նախագծի կառուցվածք.:

`typeorm init`

- Ստեղծեք դատարկ միգրացիոն ֆայլ.:

`typeorm migration:create --name {{migration_name}}`

- Ստեղծեք միգրացիոն ֆայլ SQL հայտարարություններով՝ սխեման թարմացնելու համար.:

`typeorm migration:generate --name {{migration_name}}`

- Գործարկել բոլոր առկախ միգրացիաները.:

`typeorm migration:run`

- Ստեղծեք նոր իրավաբանական ֆայլ հատուկ գրացուցակում.:

`typeorm entity:create --name {{entity}} --dir {{path/to/directory}}`

- Ցուցադրել SQL հայտարարությունները, որոնք պետք է կատարվեն `typeorm schema:sync`-ով լռելյայն կապի վրա.:

`typeorm schema:log`

- Կատարեք հատուկ SQL հայտարարություն լռելյայն կապի վրա.:

`typeorm query {{sql_sentence}}`

- Ցուցադրել օգնություն ենթահրամանի համար.:

`typeorm {{subcommand}} --help`
