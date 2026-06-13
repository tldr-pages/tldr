# bleachbit_console

> Limpia archivos basura en el sistema de archivos.
> Más información: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Inicia la versión de interfaz gráfica de usuario (GUI) de Bleachbit:

`bleachbit_console.exe --gui`

- Destruye un archivo:

`bleachbit_console.exe --shred {{ruta/al/archivo}}`

- Lista las opciones de limpieza disponibles:

`bleachbit_console.exe --list-cleaners`

- Previsualiza los archivos que se eliminarán y otros cambios que se realizarán antes de llevar a cabo la operación de limpieza:

`bleachbit_console.exe --preview {{--preset|cleaner1.opción1 cleaner2.* ...}}`

- Realiza la operación de limpieza y eliminar archivos:

`bleachbit_console.exe --clean {{--preset|cleaner1.opción1 cleaner2.* ...}}`
