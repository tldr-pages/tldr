# xml canonic

> Convierte documentos XML en canónicos.
> Más información: <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139560880>.

- Convierte un documento XML en canónico, conservando los comentarios:

`xml {{[c14n|canonic]}} {{ruta/a/entrada.xml|uri}} >{{ruta/a/salida.xml}}`

- Convierte un documento XML en canónico, eliminando los comentarios:

`xml {{[c14n|canonic]}} --without-comments {{ruta/a/entrada.xml|uri}} >{{ruta/a/salida.xml}}`

- Convertir un documento XML exclusivamente en canónico, utilizando una expresión XPATH de un archivo y conservando los comentarios:

`xml {{[c14n|canonic]}} --exc-with-comments {{ruta/a/entrada.xml|uri}} {{ruta/a/c14n.xpath}}`

- Muestra la ayuda:

`xml {{[c14n|canonic]}} --help`
