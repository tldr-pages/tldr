# apkeep

> Descarga archivos APK de varias fuentes.
> Más información: <https://github.com/EFForg/apkeep/blob/master/USAGE>.

- Descarga un archivo APK al directorio especificado:

`apkeep --app {{com.example.application}} {{ruta/al/directorio}}`

- Lista todas las versiones disponibles para descarga:

`apkeep --app {{com.example.application}} --list-versions {{ruta/al/directorio}}`

- Especifica la tienda para hacer la descarga:

`apkeep --app {{com.example.application}} --download-source {{apk-pure|google-play|f-droid|huawei-app-gallery}} {{ruta/al/directorio}}`
