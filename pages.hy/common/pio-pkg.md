# pio pkg

> Կառավարեք փաթեթները ռեեստրում:.
> Փաթեթները կարող են հեռացվել միայն դրանց հրապարակման օրվանից 72 ժամվա ընթացքում (3 օր):.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/package/>:.

- Ստեղծեք փաթեթ tarball ընթացիկ գրացուցակից.:

`pio pkg pack {{[-o|--output]}} {{path/to/package.tar.gz}}`

- Ստեղծեք և հրապարակեք փաթեթի tarball ընթացիկ գրացուցակից.:

`pio pkg publish`

- Հրապարակեք ընթացիկ գրացուցակը և սահմանափակեք դրա հանրային մուտքը.:

`pio pkg publish --private`

- Հրապարակեք փաթեթ.:

`pio pkg publish {{path/to/package.tar.gz}}`

- Հրապարակեք փաթեթ՝ հատուկ թողարկման ամսաթվով (UTC).:

`pio pkg publish {{path/to/package.tar.gz}} --released-at "{{2021-04-08 21:15:38}}"`

- Հեռացրեք հրապարակված փաթեթի բոլոր տարբերակները գրանցամատյանից.:

`pio pkg unpublish {{package}}`

- Հեռացրեք հրապարակված փաթեթի հատուկ տարբերակը գրանցամատյանից.:

`pio pkg unpublish {{package}}@{{version}}`

- Չեղարկեք հեռացումը, բոլոր տարբերակները կամ փաթեթի կոնկրետ տարբերակը նորից դնելով ռեեստր.:

`pio pkg unpublish --undo {{package}}@{{version}}`
