# ROPgadget

> Գտեք ROP գործիքներ երկուական ֆայլերում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/JonathanSalwan/ROPgadget#usage>:.

- Թվարկեք գործիքները երկուական ֆայլում.:

`ROPgadget --binary {{path/to/binary}}`

- Զտեք գաջեթները երկուական ֆայլում `regex`-ով.:

`ROPgadget --binary {{path/to/binary}} --re {{regex}}`

- Թվարկեք գաջեթները երկուական ֆայլում, բացառությամբ նշված տեսակի.:

`ROPgadget --binary {{path/to/binary}} --{{norop|nojob|nosys}}`

- Բացառեք վատ բայթ գաջեթները երկուական ֆայլում.:

`ROPgadget --binary {{path/to/binary}} --badbytes {{byte_string}}`

- Նշեք գաջեթները մինչև նշված թվով բայթ երկուական ֆայլում.:

`ROPgadget --binary {{path/to/binary}} --depth {{nbyte}}`
