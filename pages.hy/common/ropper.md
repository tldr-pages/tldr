#թափող

> Գտեք ROP գործիքներ երկուական ֆայլերում:.
> Լրացուցիչ տեղեկություններ. <https://scoding.de/ropper/>:.

- Թվարկեք գործիքները երկուական ֆայլում.:

`ropper --file {{path/to/binary}}`

- Զտեք գաջեթները երկուական ֆայլում `regex`-ով.:

`ropper --file {{path/to/binary}} --search {{regex}}`

- Նշեք նշված տեսակի հարմարանքները երկուական ֆայլում.:

`ropper --file {{path/to/binary}} --type {{rop|job|sys|all}}`

- Բացառեք վատ բայթ գաջեթները երկուական ֆայլում.:

`ropper --file {{path/to/binary}} --badbytes {{byte_string}}`

- Թվարկեք գաջեթները մինչև նշված հրահանգների քանակը երկուական ֆայլում.:

`ropper --file {{path/to/binary}} --inst-count {{count}}`
