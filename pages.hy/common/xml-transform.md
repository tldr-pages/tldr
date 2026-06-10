# xml փոխակերպում

> Փոխակերպեք XML փաստաթղթերը՝ օգտագործելով XSLT:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139602800>:.

- Փոխակերպեք XML փաստաթուղթը՝ օգտագործելով XSL ոճաթերթ՝ փոխանցելով մեկ XPATH պարամետր և մեկ բառացի տողի պարամետր.:

`xml {{[tr|transform]}} {{path/to/stylesheet.xsl}} -p "{{Count='count(/xml/table/rec)'}}" -s {{Text="Count="}} {{path/to/input.xml|uri}}`

- Ցուցադրել օգնությունը.:

`xml {{[tr|transform]}} --help`
