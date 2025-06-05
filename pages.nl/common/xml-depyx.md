# xml depyx

> Converteer een PYX (ESIS - ISO 8879) document naar XML formaat.
> Meer informatie: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139550832>.

- Converteer een PYX (ESIS - ISO 8879) document naar XML formaat:

`xml {{[p2x|depyx]}} {{pad/naar/invoer.pyx|URI}} > {{pad/naar/uitvoer.xml}}`

- Converteer een PYX document van `stdin` naar XML formaat:

`cat {{pad/naar/invoer.pyx}} | xml {{[p2x|depyx]}} > {{pad/naar/uitvoer.xml}}`

- Toon help:

`xml {{[p2x|depyx]}} --help`
