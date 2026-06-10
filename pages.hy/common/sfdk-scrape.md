# sfdk քերել

> Փոխարկեք աղբյուրի կոդի փոփոխությունները պատչերի:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/65-maintaining-mb2/doc/command.scrape.adoc>:.

- Պահպանեք աղբյուրի փոփոխությունները որպես կարկատներ.:

`sfdk scrape`

- Նախադիտեք չեղյալ համարվող պարտավորությունների ցանկը.:

`sfdk scrape {{[-n|--dry-run]}}`

- Քերեք՝ պահպանելով բուն patches ֆայլի անունները.:

`sfdk scrape --stable`

- Քերեք կարկատները նշված ելքային գրացուցակում պահելիս.:

`sfdk scrape {{[-o|--output-dir]}} {{directory}}`

- Քերեք առանց ենթամոդուլներից պարտավորությունները հանելու՝ կարկատաններ ստեղծելուց հետո.:

`sfdk scrape --keep`
