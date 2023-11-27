# xcodebuild

> Construye proyectos Xcode.
> Más información: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Construye espacio de trabajo:

`xcodebuild -workspace {{nombre_del_espacio_de_trabajo.workspace}} -scheme {{nombre_scheme}} -configuration {{nombre_configuration}} clean build SYMROOT={{ruta_SYMROOT}}`

- Construye proyecto:

`xcodebuild -target {{nombre_target}} -configuration {{nombre_configuration}} clean build SYMROOT={{ruta_SYMROOT}}`

- Muestra los SDKs:

`xcodebuild -showsdks`
