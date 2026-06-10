# npm օրգ

> Կառավարեք կազմակերպությունները:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-org/>:.

- Ավելացրեք նոր օգտվող կազմակերպությանը.:

`npm org set {{organization_name}} {{username}}`

- Փոխել օգտատիրոջ դերը կազմակերպությունում.:

`npm org set {{organization_name}} {{username}} {{developer|admin|owner}}`

- Հեռացնել օգտատիրոջը կազմակերպությունից.:

`npm org rm {{organization_name}} {{username}}`

- Նշեք կազմակերպության բոլոր օգտվողներին.:

`npm org ls {{organization_name}}`

- Ցուցակեք կազմակերպության բոլոր օգտվողներին, թողարկեք JSON ձևաչափով.:

`npm org ls {{organization_name}} --json`

- Ցուցադրել օգտատիրոջ դերը կազմակերպությունում.:

`npm org ls {{organization_name}} {{username}}`
