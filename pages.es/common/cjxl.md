# cjxl

> Comprime imágenes a JPEG XL.
> Las extensiones de entrada aceptadas son PNG, APNG, GIF, JPEG, EXR, PPM, PFM, PAM, PGX y JXL.
> Más información: <https://github.com/libjxl/libjxl>.

- Convierte una imagen a JPEG XL:

`cjxl {{ruta/a/imagen.ext}} {{ruta/a/salida.jxl}}`

- Ajusta la calidad a sin pérdidas y maximiza la compresión de la imagen resultante:

`cjxl --distance 0 --effort 9 {{ruta/a/imagen.ext}} {{ruta/a/salida.jxl}}`

- Muestra una página de ayuda muy detallada:

`cjxl {{[-h -v -v -v -v|--help --verbose --verbose --verbose --verbose]}}`
