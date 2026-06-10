# npm գտնել-խաբել

> Բացահայտեք կրկնվող կախվածությունները `node_modules`-ում:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-find-dupes/>:.

- Թվարկեք բոլոր կրկնօրինակ փաթեթները `node_modules`-ում.:

`npm find-dupes`

- Ներառեք `devDependencies` կրկնօրինակ հայտնաբերման մեջ.:

`npm find-dupes --include dev`

- Նշեք կոնկրետ փաթեթի բոլոր կրկնօրինակ օրինակները `node_modules`-ում.:

`npm find-dupes {{package_name}}`

- Բացառեք կամընտիր կախվածությունները կրկնակի հայտնաբերումից.:

`npm find-dupes --omit optional`

- Սահմանեք ելքի գրանցման մակարդակը.:

`npm find-dupes --loglevel {{silent|error|warn|info|verbose}}`

- Արտադրեք կրկնօրինակ տեղեկատվություն JSON ձևաչափով.:

`npm find-dupes --json`

- Սահմանափակեք կրկնօրինակ որոնումը որոշակի շրջանակներով.:

`npm find-dupes --scope {{@scope1,@scope2}}`

- Բացառել հատուկ շրջանակները կրկնօրինակների հայտնաբերումից.:

`npm find-dupes --omit-scope {{@scope1,@scope2}}`
