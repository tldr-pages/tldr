# pdfinfo

> Visor de información de archivos en formato PDF (Portable Document Format).
> Más información: <https://www.xpdfreader.com/pdfinfo-man.html>.

- Imprime información del archivo PDF:

`pdfinfo {{ruta/al/archivo.pdf}}`

- Especifica la contraseña de usuario del archivo PDF para omitir las restricciones de seguridad:

`pdfinfo -upw {{contraseña}} {{ruta/al/archivo.pdf}}`

- Especifica la contraseña de propietario del archivo PDF para omitir las restricciones de seguridad:

`pdfinfo -opw {{contraseña}} {{ruta/al/archivo.pdf}}`
