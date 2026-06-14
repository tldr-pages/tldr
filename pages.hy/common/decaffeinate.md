#կոֆեինատ

> Տեղափոխեք ձեր CoffeeScript աղբյուրը ժամանակակից JavaScript:.
> Լրացուցիչ տեղեկություններ. <https://www.npmjs.com/package/decaffeinate#common-options>:.

- Փոխակերպեք CoffeeScript ֆայլը JavaScript-ի.:

`decaffeinate {{path/to/file.coffee}}`

- Փոխակերպեք CoffeeScript v2 ֆայլը JavaScript-ի.:

`decaffeinate --use-cs2 {{path/to/file.coffee}}`

- Փոխակերպեք պահանջել և `module.exports` ներմուծման և արտահանման համար.:

`decaffeinate --use-js-modules {{path/to/file.coffee}}`

- Փոխակերպեք CoffeeScript-ը՝ թույլատրելով անվանված արտահանումները.:

`decaffeinate --loose-js-modules {{path/to/file.coffee}}`
