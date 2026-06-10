# npm exec

> Կատարել երկուականներ `npm` փաթեթներից:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-exec/>:.

- Կատարեք հրամանը տեղական կամ հեռավոր `npm` փաթեթից.:

`npm {{[x|exec]}} {{command}} {{argument1 argument2 ...}}`

- Հստակորեն նշեք փաթեթը (օգտակար է, եթե կան նույն անունով մի քանի հրամաններ).:

`npm {{[x|exec]}} --package {{package}} {{command}}`

- Գործարկեք հրամանը, եթե այն առկա է ընթացիկ ճանապարհում կամ `node_modules/.bin`-ում:

`npm {{[x|exec]}} --no-install {{command}} {{argument1 argument2 ...}}`

- Կատարեք կոնկրետ հրաման՝ ճնշելով ցանկացած ելք՝ `npm`-ից.:

`npm {{[x|exec]}} --quiet {{command}} {{argument1 argument2 ...}}`

- Ցուցադրել օգնությունը.:

`npm {{[x|exec]}} --help`
