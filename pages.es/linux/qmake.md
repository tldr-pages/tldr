# qmake

> Genera Makefiles a partir de archivos de proyecto Qt.
> Más información: <https://doc.qt.io/qt-6/qmake-manual.html>.

- Genera un `Makefile` a partir de un archivo de proyecto en el directorio actual:

`qmake`

- Especifica la ubicación del `Makefile` y del archivo de proyecto:

`qmake -o {{ruta/a/Makefile}} {{ruta/al/archivo_de_proyecto.pro}}`

- Genera un archivo de proyecto por defecto:

`qmake -project`

- Compila un proyecto:

`qmake && make`

- Activa el modo de depuración:

`qmake -d`
