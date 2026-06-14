# code2 հուշում

> Ստեղծեք AI-ի պատրաստ հուշումներ կոդերի բազայից (քաղեք, զտեք և ձևաչափեք կոդ LLM-ների համար):.
> Լրացուցիչ տեղեկություններ. <https://code2prompt.dev/docs/how_to/filter_files/>:.

- Ստեղծեք հուշում ընթացիկ նախագծի համար և պատճենեք այն clipboard-ում (կանխադրված վարքագիծ).:

`code2prompt {{path/to/project}}`

- Ներառեք միայն հատուկ ֆայլեր և բացառեք գրացուցակը.:

`code2prompt {{path/to/project}} {{[-i|--include]}} "{{**/*.rs}}" {{[-e|--exclude]}} "{{tests/**}}"`

- Հուշում գրեք ֆայլի վրա՝ սեղմատախտակի փոխարեն.:

`code2prompt {{path/to/project}} {{[-O|--output-file]}} {{my_prompt.txt}}`

- Կառուցված JSON արդյունք արտադրեք.:

`code2prompt {{path/to/project}} {{[-F|--output-format]}} json`

- Օգտագործեք անհատականացված Handlebars ձևանմուշ, երբ ստեղծեք հուշում.:

`code2prompt {{path/to/project}} {{[-t|--template]}} {{my_template.hbs}}`
