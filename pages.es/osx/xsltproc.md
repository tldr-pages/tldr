# xsltproc

> Transforma XML con XSLT para producir una salida (normalmente HTML o XML).
> Más información: <http://www.xmlsoft.org/xslt/xsltproc.html>.

- Transforma un archivo XML con una hoja de estilos XSLT específica:

`xsltproc --output {{ruta/al/archivo_salida.html}} {{ruta/al/archivo_hoja_estilo.xslt}} {{ruta/al/archivo.xml}}`

- Pasa un valor a un parámetro de la hoja de estilos:

`xsltproc --output {{ruta/al/archivo_salida.html}} --stringparam "{{nombre}}" "{{value}}" {{ruta/al/archivo_hoja_estilo.xslt}} {{ruta/al/archivo_xml.xml}}`
