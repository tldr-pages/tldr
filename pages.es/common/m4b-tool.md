# m4b-tool

> Fusiona, divide y manipula archivos de audiolibros con capítulos.
> Más información: <https://github.com/sandreas/m4b-tool>.

- Crea un audiolibro con los archivos de audio del directorio de entrada:

`m4b-tool merge {{ruta/a/directorio_de_entrada}} --output-file={{ruta/a/fusionado.m4b}}`

- Hace capítulos utilizando los nombres de los archivos de entrada:

`m4b-tool merge {{ruta/a/directorio_de_entrada}} --output-file={{ruta/a/fusionado.m4b}} --use-filenames-as-chapters`
