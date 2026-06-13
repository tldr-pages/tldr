# cpdf

> Interfaz de línea de comandos para manipular documentos PDF existentes de diferentes maneras.
> Más información: <https://www.coherentpdf.com/cpdfmanual/cpdfmanual.html>.

- Selecciona las páginas 1, 2, 3 y 6 del documento fuente y las agrega en el documento objetivo:

`cpdf {{ruta/al/documento_fuente.pdf}} {{1-3,6}} -o {{ruta/al/documento_objetivo.pdf}}`

- Fusiona dos documentos en uno nuevo:

`cpdf -merge {{ruta/al/documento_fuente_uno.pdf}} {{ruta/al/documento_fuente_dos.pdf}} -o {{ruta/al/documento_objetivo.pdf}}`

- Muestra los marcadores del documento:

`cpdf -list-bookmarks {{ruta/al/documento.pdf}}`

- Divide un documento en trozos de diez páginas, escribiendo `fragmento001.pdf`, `fragmento002.pdf`, etc:

`cpdf -split {{ruta/al/documento.pdf}} -o {{ruta/al/fragmento%%%.pdf}} -chunk {{10}}`

- Encripta un documento utilizando encriptado 128bit y establece `fred` como la contraseña del propietario y `joe` como la contraseña de usuario:

`cpdf -encrypt {{128bit}} {{fred}} {{joe}} {{ruta/al/documento_fuente.pdf}} -o {{ruta/al/documento_encriptado.pdf}}`

- Desencripta un documento utilizando la contraseña del propietario (`fred`):

`cpdf -decrypt {{ruta/al/documento_encriptado.pdf}} owner={{fred}} -o {{ruta/al/documento_desencriptado.pdf}}`

- Muestra las anotaciones de un documento:

`cpdf -list-annotations {{ruta/al/documento.pdf}}`

- Crea un nuevo documento, con metadatos, a partir de uno que ya existe:

`cpdf -set-metadata {{ruta/de/los/metadatos.xml}} {{ruta/al/documento_fuente.pdf}} -o {{ruta/al/documento_objetivo.pdf}}`
