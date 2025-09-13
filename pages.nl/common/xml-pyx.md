# xml pyx

> Converteer een XML-document naar het PYX-formaat (ESIS - ISO 8879).
> Meer informatie: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139550832>.

- Converteer een XML document naar PYX formaat:

`xml pyx {{pad/naar/invoer.xml|URI}} > {{pad/naar/uitvoer.pyx}}`

- Converteer een XML document van `stdin` naar PYX formaat:

`cat {{pad/naar/invoer.xml}} | xml pyx > {{pad/naar/uitvoer.pyx}}`

- Toon de help:

`xml pyx --help`
