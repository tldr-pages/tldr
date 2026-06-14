# pdf-վերլուծիչ

> Բացահայտեք PDF ֆայլի հիմնարար տարրերը՝ առանց այն ներկայացնելու:.
> Լրացուցիչ տեղեկություններ. <https://blog.didierstevens.com/programs/pdf-tools/>:.

- Ցուցադրել վիճակագրություն PDF ֆայլի համար.:

`pdf-parser {{[-a|--stats]}} {{path/to/file.pdf}}`

- Ցուցադրել որոշակի տեսակի օբյեկտներ (`/Font`, `/URI`, ...) PDF ֆայլում.:

`pdf-parser {{[-t|--type]}} {{/object_type}} {{path/to/file.pdf}}`

- Անուղղակի օբյեկտներում տողերի որոնում.:

`pdf-parser {{[-s|--search]}} {{search_string}} {{path/to/file.pdf}}`
