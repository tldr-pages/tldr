#հետևանք

> Promise-ի վրա հիմնված Node.js ORM Postgres-ի, MySQL-ի, MariaDB-ի, SQLite-ի և Microsoft SQL Server-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://sequelize.org/docs/v7/cli/>:.

- Ստեղծեք մոդել 3 դաշտերով և միգրացիոն ֆայլով.:

`sequelize model:generate --name {{table_name}} --attributes {{field1:integer,field2:string,field3:boolean}}`

- Գործարկեք միգրացիոն ֆայլը.:

`sequelize db:migrate`

- Վերադարձեք բոլոր միգրացիաները.:

`sequelize db:migrate:undo:all`

- Տվյալների բազան համալրելու համար ստեղծեք սերմային ֆայլ նշված անունով.:

`sequelize seed:generate --name {{seed_filename}}`

- Լրացրեք տվյալների բազան՝ օգտագործելով բոլոր սերմերի ֆայլերը.:

`sequelize db:seed:all`
