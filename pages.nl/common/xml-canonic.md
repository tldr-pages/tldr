# xml canonic

> Maak XML-documenten canoniek.
> Meer informatie: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139560880>.

- Maak een XML-document canoniek met behoud van commentaar:

`xml {{[c14n|canonic]}} {{pad/naar/invoer.xml|URI}} > {{pad/naar/uitvoer.xml}}`

- Maak een XML-document canoniek en verwijder het commentaar:

`xml {{[c14n|canonic]}} --without-comments {{pad/naar/invoer.xml|URI}} > {{pad/naar/uitvoer.xml}}`

- Maak XML uitsluitend canoniek, met behulp van een XPATH vanuit een bestand, met behoud van commentaar:

`xml {{[c14n|canonic]}} --exc-with-comments {{pad/naar/invoer.xml|URI}} {{pad/naar/c14n.xpath}}`

- Toon de help:

`xml {{[c14n|canonic]}} --help`
