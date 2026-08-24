# qmake

> Genera archivos Makefile a partir de archivos de proyecto Qt.
> Más información: <https://doc.qt.io/qt-6/qmake-running.html>.

- Genera un archivo `Makefile` a partir de un archivo de proyecto en el directorio actual:

`qmake`

- Especifica las ubicaciones del archivo `Makefile` y del archivo de proyecto:

`qmake -o {{ruta/a/Makefile}} {{ruta/para/archivo_de_proyecto.pro}}`

- Genera un archivo de proyecto predeterminado:

`qmake -project`

- Compila un proyecto:

`qmake && make`

- Habilita el modo de depuración:

`qmake -d`

- Muestra la ayuda:

`qmake -help`
