# bun տեղադրում

> Տեղադրեք JavaScript-ի կախվածությունը նախագծի համար `package.json`-ից:.
> Լրացուցիչ տեղեկություններ. <https://bun.com/docs/pm/cli/install>:.

- Տեղադրեք `package.json`-ում թվարկված բոլոր կախվածությունները՝:

`bun {{[i|install]}}`

- Տեղադրեք մեկ փաթեթ (սա `bun add`-ի կեղծանունն է).:

`bun {{[i|install]}} {{package_name}}@{{version}}`

- Տեղադրեք փաթեթ ամբողջ աշխարհում.:

`bun {{[i|install]}} {{[-g|--global]}} {{package_name}}`

- Տեղադրեք միայն արտադրական կախվածությունները (բաց թողնում `devDependencies`):

`bun {{[i|install]}} {{[-p|--production]}}`

- Տեղադրեք կախվածությունները հենց `bun.lockb` lockfile-ից (սառեցված lockfile):

`bun {{[i|install]}} --frozen-lockfile`

- Ստիպեք նորից ներբեռնել բոլոր փաթեթները ռեեստրից՝ անտեսելով քեշը.:

`bun {{[i|install]}} {{[-f|--force]}}`
