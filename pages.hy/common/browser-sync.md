# դիտարկիչ-համաժամեցում

> Տեղական վեբ սերվեր, որը թարմացնում է բրաուզերը ֆայլերի փոփոխությունների վերաբերյալ:.
> Լրացուցիչ տեղեկություններ. <https://browsersync.io/docs/command-line>:.

- Սկսեք սերվերը որոշակի գրացուցակից.:

`browser-sync start --server {{path/to/directory}} --files {{path/to/directory}}`

- Սկսեք սերվեր տեղական գրացուցակից՝ դիտելով բոլոր CSS ֆայլերը գրացուցակում.:

`browser-sync start --server --files '{{path/to/directory/*.css}}'`

- Ստեղծեք կազմաձևման ֆայլ.:

`browser-sync init`

- Սկսեք Browsersync-ը կազմաձևման ֆայլից.:

`browser-sync start --config {{config_file}}`
