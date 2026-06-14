# corepack

> Զրոյական գործարկման կախվածության փաթեթ, որը գործում է որպես կամուրջ Node նախագծերի և դրանց փաթեթների կառավարիչների միջև:.
> Լրացուցիչ տեղեկություններ. <https://github.com/nodejs/corepack>:.

- Ավելացնել Corepack shims-ը Node.js-ի տեղադրման գրացուցակում՝ դրանք հասանելի դարձնելու որպես գլոբալ հրամաններ.:

`corepack enable`

- Ավելացնել Corepack shims-ը որոշակի գրացուցակում.:

`corepack enable --install-directory {{path/to/directory}}`

- Հեռացրեք Corepack shims-ը Node.js տեղադրման գրացուցակից.:

`corepack disable`

- Պատրաստեք հատուկ փաթեթի կառավարիչ.:

`corepack prepare {{package_manager}}@{{version}} --activate`

- Պատրաստեք փաթեթի կառավարիչը, որը կազմաձևված է նախագծի համար ընթացիկ ճանապարհով.:

`corepack prepare`

- Օգտագործեք փաթեթի կառավարիչ՝ առանց այն որպես գլոբալ հրաման տեղադրելու.:

`corepack {{npm|pnpm|yarn}} {{package_manager_arguments}}`

- Տեղադրեք փաթեթի կառավարիչ նշված արխիվից.:

`corepack hydrate {{path/to/corepack.tgz}}`

- Ցուցադրել օգնություն ենթահրամանի համար.:

`corepack {{subcommand}} --help`
