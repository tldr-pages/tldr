#զինտ

> Ստեղծեք շտրիխ կոդեր և QR կոդեր:.
> Լրացուցիչ տեղեկություններ. <https://www.zint.org.uk/manual/chapter/4>:.

- Ստեղծեք շտրիխ կոդ և պահպանեք այն.:

`zint --data "{{UTF-8 data}}" --output {{path/to/file}}`

- Նշեք կոդերի տեսակը սերնդի համար.:

`zint --barcode {{code_type}} --data "{{UTF-8 data}}" --output {{path/to/file}}`

- Թվարկեք բոլոր աջակցվող կոդերի տեսակները.:

`zint --types`
