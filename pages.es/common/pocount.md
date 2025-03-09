# pocount

> Utilidad de Translate Toolkit para obtener el progreso de la traducción de un archivo, soporta varios formatos.
> Más información: <https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pocount.html>.

- Imprime una tabla colorida con el progreso de la traducción de un archivo:

`pocount {{ruta/al/archivo.po}}`

- Imprime el progreso de las traducciones de varios archivos, una línea por archivo:

`pocount --short {{traducción_*.ts}}`

- Genera un archivo CSV con el progreso de la traducción de varios archivos:

`pocount --csv {{traducción_*.ts}} > {{ruta/a/progreso_de_traducción.csv}}`
