# վեբ-ext

> Կառավարեք վեբ ընդլայնման զարգացումը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/mozilla/web-ext>:.

- Գործարկեք վեբ ընդլայնումը Firefox-ի ընթացիկ գրացուցակում.:

`web-ext run`

- Գործարկեք վեբ ընդլայնում Firefox-ի որոշակի գրացուցակից.:

`web-ext run --source-dir {{path/to/directory}}`

- Ցուցադրել ծավալուն կատարման արդյունքը.:

`web-ext run --verbose`

- Գործարկել վեբ ընդլայնում Firefox Android-ում.:

`web-ext run --target firefox-android`

- Սխալների համար փակցրեք մանիֆեստը և աղբյուրի ֆայլերը.:

`web-ext lint`

- Կառուցեք և փաթեթավորեք ընդլայնումը.:

`web-ext build`

- Ցուցադրել ծավալուն կառուցման արդյունքը.:

`web-ext build --verbose`

- Ինքնահոսթինգի փաթեթ ստորագրեք.:

`web-ext sign --api-key {{api_key}} --api-secret {{api_secret}}`
