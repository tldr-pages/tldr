# sips

> Sistema de procesamiento de imágenes Apple Scriptable.
> Imágenes Raster/Query y Perfiles ICC ColorSync.
> Más información: <https://ss64.com/osx/sips.html>.

- Especifica un directorio de salida para que los originales no se modifiquen:

`sips --out {{ruta/al/directorio_salida}}`

- Remuestrea la imagen al tamaño especificado, la relación de aspecto de la imagen puede verse alterada:

`sips --resampleHeightWidth {{1920}}} {{300}} {{archivo_imagen.ext}}`

- Remuestrea la imagen para que la altura y la anchura no superen el tamaño especificado (fíjate en la Z mayúscula):

`sips --resampleHeightWidthMax {{1920}}} {{300}} {{archivo_imagen.ext}}`

- Remuestrea todas las imágenes de un directorio para que se ajusten a una anchura de 960px (respetando la relación de aspecto):

`sips --resampleWidth {{960}} {{ruta/al/imágenes}}`

- Convierte una imagen de CMYK a RGB:

`sips --matchTo "/System/Library/ColorSync/Profiles/Generic RGB Profile.icc" {{ruta/al/imagen.ext}} {{ruta/al/directorio_salida}}`

- Elimina el perfil ICC ColorSync de una imagen:

`sips --deleteProperty profile --deleteColorManagementProperties {{ruta/al/archivo_de_imagen.ext}}`
