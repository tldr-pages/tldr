# npm տեղադրում

> Տեղադրեք Node փաթեթներ:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-install/>:.

- Տեղադրեք `package.json`-ում թվարկված կախվածությունները՝:

`npm {{[i|install]}}`

- Ներբեռնեք փաթեթի որոշակի տարբերակ և ավելացրեք այն `package.json`-ի կախվածությունների ցանկում՝:

`npm {{[i|install]}} {{package_name}}@{{version}}`

- Ներբեռնեք փաթեթի վերջին տարբերակը և ավելացրեք այն մշակողի կախվածությունների ցանկում `package.json`-ում:

`npm {{[i|install]}} {{package_name}} {{[-D|--save-dev]}}`

- Ներբեռնեք փաթեթի վերջին տարբերակը և տեղադրեք այն ամբողջ աշխարհում (սահմանեք տեղադրման վայրը `npm config set prefix`-ով):

`npm {{[i|install]}} {{package_name}} {{[-g|--global]}}`
