# wlc

> Կառավարեք տեղայնացման նախագծերը Weblate-ի օրինակում:.
> Լրացուցիչ տեղեկություններ. <https://docs.weblate.org/en/latest/wlc.html#commands>:.

- Թվարկեք նախագծերը, օգտագործելով կազմաձևման ֆայլը.:

`wlc {{[-c|--config]}} {{path/to/file}} list-projects`

- Ցուցակեք բաղադրիչները նախագծի մեջ և վերացրեք API URL-ը և API բանալին.:

`wlc {{[-u|--url]}} {{url}} {{[-k|--key]}} {{key}} ls {{project}}`

- Ցուցակեք թարգմանությունները բաղադրիչից հատուկ ձևաչափով.:

`wlc {{[-f|--format]}} {{text|csv|json|html}} ls {{project}}/{{component}}`

- Տպել վիճակագրություն նախագծի համար.:

`wlc stats {{project}}`

- Ցուցադրել օգնությունը.:

`wlc {{[-h|--help]}}`
