# sqlx

> Կոմունալ SQLx-ի համար, Rust SQL գործիքակազմը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/launchbadge/sqlx/blob/main/sqlx-cli/README.md>:.

- Ստեղծեք `$DATABASE_URL` միջավայրի փոփոխականում նշված տվյալների բազա.:

`sqlx database create`

- Բաց թողեք նշված տվյալների բազան.:

`sqlx database drop {{[-D|--database-url]}} {{database_url}}`

- Ստեղծեք նոր զույգ վեր և վար միգրացիոն ֆայլեր՝ տրված նկարագրությամբ «միգրացիաներ» գրացուցակում.:

`sqlx migrate add -r {{migration_description}}`

- Գործարկեք բոլոր սպասող միգրացիաները նշված տվյալների բազայի համար.:

`sqlx migrate run {{[-D|--database-url]}} {{database_url}}`

- Վերադարձեք վերջին միգրացիան նշված տվյալների բազայի համար.:

`sqlx migrate revert {{[-D|--database-url]}} {{database_url}}`
