#fastmod

> `codemod` գործիքի արագ մասնակի փոխարինում, փոխարինեք և փոխարինեք բոլորը ամբողջ կոդերի բազայում:.
> Ռեգեքսները համընկնում են Rust `regex` տուփով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/facebookincubator/fastmod>:.

- Փոխարինեք `regex`-ը ընթացիկ գրացուցակի բոլոր ֆայլերում՝ անտեսելով `.ignore` և `.gitignore` ֆայլերը:

`fastmod {{regex}} {{replacement}}`

- Փոխարինեք `regex`-ը հատուկ ֆայլերում կամ գրացուցակներում մեծատառերի անզգայուն ռեժիմում.:

`fastmod --ignore-case {{regex}} {{replacement}} -- {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Փոխարինեք `regex`-ը կոնկրետ գրացուցակում, ֆայլերում, որոնք զտված են մեծատառերի անզգայուն գլոբուսի օրինակով.:

`fastmod {{regex}} {{replacement}} --dir {{path/to/directory}} --iglob '{{**/*.{js,json}}}'`

- Փոխարինեք ճշգրիտ տողի համար `.js` կամ JSON ֆայլերում.:

`fastmod --fixed-strings {{exact_string}} {{replacement}} --extensions {{json,js}}`

- Փոխարինեք ճշգրիտ տողով առանց հաստատման հուշման (անջատում է `regex`):

`fastmod --accept-all --fixed-strings {{exact_string}} {{replacement}}`

- Փոխարինեք ճշգրիտ տողի համար՝ առանց հաստատման հուշման, փոխված ֆայլերի տպում.:

`fastmod --accept-all --print-changed-files --fixed-strings {{exact_string}} {{replacement}}`
