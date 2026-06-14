# xml depyx

> Փոխարկել PYX (ESIS - ISO 8879) փաստաթուղթը XML ձևաչափի:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139550832>:.

- Փոխակերպեք PYX (ESIS - ISO 8879) փաստաթուղթը XML ձևաչափի.:

`xml {{[p2x|depyx]}} {{path/to/input.pyx|uri}} > {{path/to/output.xml}}`

- Փոխակերպեք PYX փաստաթուղթը `stdin`-ից XML ձևաչափի.:

`cat {{path/to/input.pyx}} | xml {{[p2x|depyx]}} > {{path/to/output.xml}}`

- Ցուցադրել օգնությունը.:

`xml {{[p2x|depyx]}} --help`
