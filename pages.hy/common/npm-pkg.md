# npm pkg

> Ցույց տալ կամ փոփոխել `package.json` հատկությունները:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-pkg/>:.

- Ստացեք որոշակի գույքի արժեքը.:

`npm pkg get {{name}}`

- Միանգամից ստացեք բազմաթիվ հատկություններ.:

`npm pkg get {{name|version|...}}`

- Ստացեք բազմաթիվ արժեքներ բոլոր աշխատանքային տարածքներում.:

`npm pkg get {{name}} {{version}} {{[--ws|--workspaces]}}`

- Ստացեք ներդիր կամ զանգվածային հատկության արժեքը.:

`npm pkg get {{contributors[0].email}}`

- Սահմանեք հատկությունը որոշակի արժեքի.:

`npm pkg set {{property}}={{value}}`

- Միանգամից մի քանի հատկություններ սահմանեք.:

`npm pkg set {{property1}}={{value1}} {{property2}}={{value2}}`

- Ջնջել հատկությունը `package.json`-ից՝:

`npm pkg delete {{scripts.build}}`

- Ավտոմատ շտկել `package.json`-ի ընդհանուր սխալները.:

`npm pkg fix`
