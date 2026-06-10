# npm dedude

> Կրճատեք կրկնօրինակումը `node_modules` գրացուցակում:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-dedupe/>:.

- Կրկնօրինակեք փաթեթները `node_modules`-ում՝:

`npm {{[ddp|dedupe]}}`

- Հետևեք `package-lock.json`-ին կամ `npm-shrinkwrap.json`-ին կրկնօրինակման ժամանակ.:

`npm {{[ddp|dedupe]}} --lock`

- Գործարկեք կրկնօրինակումը խիստ ռեժիմով.:

`npm {{[ddp|dedupe]}} --strict`

- Բաց թողնել կամընտիր/հասակակից կախվածությունները կրկնօրինակման ժամանակ.:

`npm {{[ddp|dedupe]}} --omit {{optional|peer}}`

- Միացնել մանրամասն գրանցումը անսարքությունների վերացման համար.:

`npm {{[ddp|dedupe]}} --loglevel verbose`

- Սահմանափակեք կրկնօրինակումը որոշակի փաթեթով.:

`npm {{[ddp|dedupe]}} {{package_name}}`
