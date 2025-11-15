# xctool

> Herramienta para construir proyectos Xcode.
> Más información: <https://github.com/facebookarchive/xctool>.

- Construye un proyecto sin ningún espacio de trabajo:

`xctool -project {{TuProyecto.xcodeproj}} -scheme {{SuEsquema}} build`

- Construye un proyecto que forma parte de un espacio de trabajo:

`xctool -workspace {{TuEspacioDeTrabajo.xcworkspace}} -scheme {{TuEsquema}} build`

- Limpia, construye y ejecuta todas las pruebas:

`xctool -workspace {{TuEspacioTrabajo.xcworkspace}} -scheme {{TuEsquema}} clean build test`
