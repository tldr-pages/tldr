# sfdk կառուցել-պահանջվում է

> Թարմացրեք կառուցման ժամանակի կախվածությունը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/20-building-mb2/doc/command.build-requires.adoc>:.

- Գործարկեք ենթահրաման, որը թարմացնում է քեշը.:

`sfdk build-requires --refresh {{subcommand}}`

- Գործարկեք ենթահրաման առանց քեշը թարմացնելու.:

`sfdk build-requires --no-refresh {{subcommand}}`

- Տեղադրեք կամ թարմացրեք կառուցման ժամանակի կախվածությունները.:

`sfdk build-requires pull`

- Տեղադրեք կամ թարմացրեք կառուցման ժամանակի կախվածությունները՝ բաց թողնելով բոլոր լրացուցիչները.:

`sfdk build-requires reset`

- Ցույց տալ տարբերությունը ընթացիկ և մաքուր շինարարական միջավայրերի միջև.:

`sfdk build-requires diff`
