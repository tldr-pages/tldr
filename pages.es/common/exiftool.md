# exiftool

> Lee y escribe metainformación en archivos.
> Más información: <https://exiftool.org/exiftool_pod.html>.

- Muestra los metadatos EXIF de un archivo dado:

`exiftool {{ruta/al/archivo}}`

- Elimina todos los metadatos EXIF de los archivos dados:

`exiftool -All= {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Elimina los metadatos EXIF de GPS de los archivos de imagen dados:

`exiftool "-gps*=" {{ruta/a/imagen1 ruta/a/imagen2 ...}}`

- Elimina todos los metadatos EXIF de los archivos de imagen dados y luego vuelve a añadir los metadatos de color y orientación:

`exiftool -All= -tagsfromfile @ -colorspacetags -orientation {{ruta/a/imagen1 ruta/a/imagen2 ...}}`

- Adelanta 1 hora la fecha en que se tomaron todas las fotos de un directorio:

`exiftool "-AllDates+=0:0:0 1:0:0" {{ruta/al/directorio}}`

- Retrasa 1 día y 2 horas la fecha en que se tomaron todas las fotos JPEG del directorio actual:

`exiftool "-AllDates-=0:0:1 2:0:0" {{[-ext|-extension]}} jpg`

- Modifica únicamente el campo `DateTimeOriginal` restando 1,5 horas, sin mantener copias de seguridad:

`exiftool -DateTimeOriginal-=1.5 -overwrite_original`

- Renombra de forma recursiva todas las fotos JPEG de un directorio según el campo `DateTimeOriginal`:

`exiftool '-filename<DateTimeOriginal' {{[-d|-dateFormat]}} %Y-%m-%d_%H-%M-%S%%lc.%%e {{ruta/al/directorio}} {{[-r|-recurse]}} {{[-ext|-extension]}} jpg`
