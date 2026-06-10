#փոխանցում

> Փոխանցման համար ոչ պաշտոնական հաճախորդ.sh.
> Լրացուցիչ տեղեկություններ. <https://github.com/AlpixTM/transfersh>:.

- Վերբեռնեք ֆայլ transfer.sh-ում:

`transfersh {{path/to/file}}`

- Վերբեռնեք առաջընթացի տող ցուցադրող ֆայլ (պահանջվում է Python փաթեթ `requests_toolbelt`):

`transfersh {{[-p|--progress]}} {{path/to/file}}`

- Վերբեռնեք ֆայլ՝ օգտագործելով այլ ֆայլի անուն.:

`transfersh {{[-n|--name]}} {{filename}} {{path/to/file}}`

- Վերբեռնեք ֆայլ մաքսային transfer.sh սերվեր.:

`transfersh {{[-sn|--servername]}} {{upload.server.name}} {{path/to/file}}`

- Վերբեռնեք բոլոր ֆայլերը գրացուցակից ռեկուրսիվ կերպով.:

`transfersh {{[-r|--recursive]}} {{path/to/directory}}/`

- Վերբեռնեք որոշակի գրացուցակ որպես չսեղմված tar:

`transfersh {{[-rt|--recursive --tar]}} {{path/to/directory}}`
