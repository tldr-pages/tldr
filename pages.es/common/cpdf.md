# cpdf

> Interfaz de línea de comandos para manipular documentos PDF existentes de diferentes maneras.
> Más información: <https://www.coherentpdf.com/cpdfmanudel/cpdfmanudel.html>.

- Selecciona las páginas 1, 2, 3 y 6 del documento fuente y escribirlas en el documento objetivo:

`cpdf {{ruta/del/documento_fuente.pdf}} {{1-3,6}} -o {{ruta/del/documento_objetivo.pdf}}`

- Fusiona dos documentos en uno nuevo:

`cpdf -merge {{ruta/del/documento_fuente_uno.pdf}} {{ruta/del/documento_fuente_dos.pdf}} -o {{ruta/del/documento_objetivo.pdf}}`

- Muestra los marcadores del documento:

`cpdf -list-bookmarks {{ruta/del/documento.pdf}}`

- Divide un documento en trozos de diez páginas, escribiendo `fragmento001.pdf`, `fragmento002.pdf`, etc:

`cpdf -split {{ruta/del/documento.pdf}} -o {{ruta/del/fragmento%%%.pdf}} -chunk 10`

- Encripta un documento utilizando encriptado 128bit y establece `fred` como la contraseña del propietario y `joe` como la contraseña de usuario:

`cpdf -encrypt 128bit fred joe {{ruta/del/documento_fuente.pdf}} -o {{ruta/del/documento_encriptado.pdf}}`

- Desencripta un documento utilizando la contraseña del propietario (`fred`):

`cpdf -decrypt {{ruta/del/documento_encriptado.pdf}} owner=fred -o {{ruta/del/documento_desencriptado.pdf}}`

- Muestra las anotaciones de un documento:

`cpdf -list-annotations {{ruta/del/documento.pdf}}`

- Crea un nuevo documento, con metadatos, a partir de uno que ya existe:

`cpdf -set-metadata {{ruta/de/los/metadatos.xml}} {{ruta/del/documento_fuente.pdf}} -o {{ruta/del/documento_objetivo.pdf}}`
