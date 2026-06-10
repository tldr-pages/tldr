# gh երկնագիծ

> Ստեղծեք ձեր GitHub ներդրման պատմության 3D մոդելը:.
> Լռելյայնորեն, այն ընթացիկ գրացուցակում կստեղծի `{username}-{year}-github-skyline.stl` ֆայլ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/github/gh-skyline>:.

- Ստեղծեք skyline STL ֆայլ ընթացիկ տարվա և վավերացված օգտվողի համար.:

`gh skyline`

- Ստեղծեք ուրվագիծ որոշակի օգտագործողի և տարվա համար.:

`gh skyline {{[-u|--user]}} {{username}} {{[-y|--year]}} {{year}}`

- Ստեղծեք տեսարան մի քանի տարիների ընթացքում.:

`gh skyline {{[-u|--user]}} {{username}} {{[-y|--year]}} {{first_year}}-{{last_year}}`

- Ստեղծեք ամբողջական ուրվագիծ (օգտագործողի միանալու տարվանից մինչև ընթացիկ տարի).:

`gh skyline {{[-u|--user]}} {{username}} {{[-f|--full]}}`

- Միացնել վրիպազերծման գրանցումը.:

`gh skyline {{[-d|--debug]}}`

- Ստեղծեք հորիզոն և նշեք ելքային ֆայլի ուղին.:

`gh skyline {{[-o|--output]}} {{path/to/output_file.stl}}`

- Բացեք GitHub պրոֆիլը որոշակի օգտվողի համար.:

`gh skyline {{[-u|--user]}} {{username}} {{[-w|--web]}}`

- Ցուցադրել օգնությունը.:

`gh skyline {{[-h|--help]}}`
