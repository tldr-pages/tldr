# xdelta

> Դելտա կոդավորման ծրագիր՝ երկուական ֆայլերի վրա patches ստեղծելու և կիրառելու համար:.
> Ժամանակակից տարբերակի համար (v3) տես `xdelta3`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/xdelta>:.

- Ստեղծեք կարկատել (դելտա) երկու ֆայլերի միջև.:

`xdelta delta {{path/to/old_file}} {{path/to/new_file}} {{path/to/patch_file}}`

- Կիրառեք կարկատել հին ֆայլի վրա՝ նոր ֆայլը վերակառուցելու համար.:

`xdelta patch {{path/to/patch_file}} {{path/to/old_file}} {{path/to/new_file}}`

- Ստեղծեք կարկատել հատուկ սեղմման մակարդակով.:

`xdelta delta -{{0..9}} {{path/to/old_file}} {{path/to/new_file}} {{path/to/patch_file}}`
