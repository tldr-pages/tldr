#սերիալ

> Վերադարձնում է դասերի serialVersionUID-ը:.
> Այն լռելյայն չի սահմանում անվտանգության կառավարիչ:.
> Լրացուցիչ տեղեկություններ. <https://docs.oracle.com/en/java/javase/25/docs/specs/man/serialver.html>:.

- Ցուցադրել դասի serialVersionUID-ը.:

`serialver {{classnames}}`

- Ցուցադրել serialVersionUID-ը դասերի և ռեսուրսների երկու կետով առանձնացված ցանկի համար.:

`serialver -classpath {{path/to/directory}} {{classname1:classname2:...}}`

- Օգտագործեք հատուկ տարբերակ Java հավելվածի գործարկիչի տեղեկատու էջից դեպի Java վիրտուալ մեքենա.:

`serialver -Joption {{classnames}}`
