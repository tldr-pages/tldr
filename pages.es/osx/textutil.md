# textutil

> Manipula archivos de texto en varios formatos.
> Más información: <https://keith.github.io/xcode-man-pages/textutil.1.html>.

- Muestra información de `foo.rtf`:

`textutil -info {{foo.rtf}}`

- Convierte `foo.rtf` en `foo.html`:

`textutil -convert {{html}} {{foo.rtf}}`

- Convierte texto enriquecido a texto normal:

`textutil {{foo.rtf}} -convert {{txt}}`

- Convierte `foo.txt` en `foo.rtf`, usando la fuente Times con un tamaño 10:

`textutil -convert {{rtf}} -font {{Times}} -fontsize {{10}} {{foo.txt}}`

- Carga todos los archivos RTF en el directorio actual, concatena su contenido y escribe el resultado como `index.html` con el título HTML establecido en "Varios archivos":

`textutil -cat {{html}} -title "Varios archivos" -output {{index.html}} *.rtf`
