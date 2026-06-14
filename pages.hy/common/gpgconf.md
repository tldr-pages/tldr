# gpgconf

> Փոփոխել `.gnupg` տնային գրացուցակները:.
> Լրացուցիչ տեղեկություններ. <https://www.gnupg.org/documentation/manuals/gnupg/gpgconf.html>:.

- Նշեք բոլոր բաղադրիչները.:

`gpgconf --list-components`

- Թվարկեք gpgconf-ի կողմից օգտագործվող դիրեկտորիաները.:

`gpgconf {{[-L|--list-dirs]}}`

- Նշեք բաղադրիչի բոլոր տարբերակները.:

`gpgconf --list-options {{component}}`

- Թվարկեք ծրագրերը և ստուգեք, թե արդյոք դրանք գործարկվում են.:

`gpgconf --check-programs`

- Վերբեռնեք բաղադրիչը.:

`gpgconf --reload {{component}}`
