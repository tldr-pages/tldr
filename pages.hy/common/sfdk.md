# sfdk

> Sailfish SDK-ի ճակատը:.
> Որոշ ենթահրամաններ, ինչպիսիք են `init`, `build-init`, `device`, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/10-general/doc/module.adoc>:.

- Ստեղծեք ներկայիս միջավայրը SailfishOS-ի համար հատուկ տարբերակներով և ճարտարապետական նպատակներով կառուցելու համար.:

`sfdk config target=SailfishOS-{{5.0.0.62}}-{{aarch64}}`

- Նախաձեռնեք ընթացիկ գրացուցակը որպես կառուցման գրացուցակ.:

`sfdk build-init`

- Կատարեք RPM SPEC ֆայլի կառուցման քայլերը կոնկրետ նախագծի համար.:

`sfdk -C {{path/to/project}} build`

- Թվարկեք պահոցները SailfishOS 5.0.0.62 armv7hl կառուցման թիրախում.:

`sfdk -c 'target=SailfishOS-5.0.0.62-armv7hl' build-shell --maintain ssu lr`

- Տեղադրեք փաթեթը էմուլյատորին.:

`sfdk config device="{{Sailfish OS Emulator 5.0.0.62}}"; sfdk deploy --sdk`

- Ցուցադրել օգնությունը.:

`sfdk --help`

- Ցուցադրել օգնություն կոնկրետ թեմայի համար (`building`, `testing`, `maintaining`, `ide`, `all`):

`sfdk --help-{{topic}}`

- Ցուցադրման տարբերակը:

`sfdk --version`
