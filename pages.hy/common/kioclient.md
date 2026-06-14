# kioclient

> Կատարել ցանցային թափանցիկ ֆայլերի գործողություններ՝ օգտագործելով KDE-ի KIO ենթահամակարգը:.
> Աջակցում է URL սխեմաներին, ինչպիսիք են `file:`, `sftp:`, `smb:`, `fish:` և `trash:`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/kioclient>:.

- Բացեք URL իր լռելյայն KDE կարգավորիչով.:

`kioclient exec {{url}}`

- Տպեք հեռակա ֆայլի բովանդակությունը `stdout`-ում՝:

`kioclient cat {{sftp://user@host/path/to/file}}`

- Թվարկեք հեռավոր գրացուցակի բովանդակությունը.:

`kioclient ls {{smb://server/share}}`

- Պատճենեք մեկ կամ մի քանի ֆայլ KIO-ի միջոցով.:

`kioclient cp {{path/to/source1 path/to/source2 ...}} {{path/to/destination}}`

- Տեղափոխեք ֆայլը KIO-ի միջոցով.:

`kioclient mv {{path/to/source}} {{path/to/destination}}`

- Հեռացրեք ֆայլը KIO-ի միջոցով.:

`kioclient rm {{url}}`

- Ստեղծեք նոր գրացուցակ KIO-ի միջոցով.:

`kioclient mkdir {{url}}`

- Ցուցադրել օգնությունը.:

`kioclient --help`
