# plutil

> Ve, convierte, valida o edita archivos de listas de propiedades ("plist").
> Más información: <https://www.manpagez.com/man/1/plutil/>.

- Muestra el contenido de uno o más archivos plist en un formato legible por humanos:

`plutil -p {{archivo1.plist archivo2.plist ...}}`

- Convierte uno o varios archivos plist a formato XML, sobrescribiendo los archivos originales:

`plutil -convert xml1 {{archivo1.plist archivo2.plist ...}}`

- Convierte uno o más archivos plist a formato binario, sobrescribiendo los archivos originales en su lugar:

`plutil -convert binary1 {{archivo1.plist archivo2.plist ...}}`

- Convierte un archivo plist a un formato diferente, escribiendo en un nuevo archivo:

`plutil -convert {{xml1|binary1|json|swift|objc}} {{ruta/al/archivo.plist}} -o {{ruta/al/nuevo_archivo.plist}}`

- Convierte un archivo plist a un formato diferente, escribiendo en `stdout`:

`plutil -convert {{xml1|binary1|json|swift|objc}} {{ruta/al/archivo.plist}} -o -`
