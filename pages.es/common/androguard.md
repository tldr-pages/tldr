# androguard

> Obtiene información o un diseño a partir de una aplicación de Android. Escrito en Python.
> Más información: <https://github.com/androguard/androguard>.

- Despliega el manifiesto de la aplicación Android:

`androguard axml {{ruta/al/app.apk}}`

- Despliega metadatos de la aplicación (versión y ID de la app):

`androguard apkid {{ruta/a/app.apk}}`

- Descompila el código en Java de una aplicación:

`androguard decompile {{ruta/a/app.apk}} --output {{ruta/al/directorio_de_salida}}`
