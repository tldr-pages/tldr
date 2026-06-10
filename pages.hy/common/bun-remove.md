# բուլկի հեռացնել

> Հեռացրեք կախվածությունը `package.json`-ից:.
> Լրացուցիչ տեղեկություններ. <https://bun.com/docs/pm/cli/remove>:.

- Հեռացնել կախվածությունը.:

`bun {{[rm|remove]}} {{package_name}}`

- Հեռացրեք բազմաթիվ կախվածությունները.:

`bun {{[rm|remove]}} {{package_name1 package_name2 ...}}`

- Հեռացրեք գլոբալ տեղադրված փաթեթը.:

`bun {{[rm|remove]}} {{[-g|--global]}} {{package_name}}`

- Հեռացրեք կախվածությունը՝ առանց `package.json` ֆայլի թարմացման.:

`bun {{[rm|remove]}} --no-save {{package_name}}`

- Գործարկեք հրամանը առանց փաթեթները իրականում հեռացնելու (նմանացրեք հեռացումը).:

`bun {{[rm|remove]}} --dry-run {{package_name}}`
