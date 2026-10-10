# xml depyx

> Convierte un documento PYX (ESIS - ISO 8879) al formato XML.
> Más información: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139550832>.

- Convierte un documento PYX (ESIS - ISO 8879) a formato XML:

`xml {{[p2x|depyx]}} {{ruta/al/input.pyx|uri}} > {{ruta/al/output.xml}}`

- Convierte un documento PYX desde `stdin` a formato XML:

`cat {{ruta/a/input.pyx}} | xml {{[p2x|depyx]}} > {{ruta/a/output.xml}}`

- Muestra la ayuda:

`xml {{[p2x|depyx]}} --help`
