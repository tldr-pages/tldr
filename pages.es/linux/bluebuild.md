# bluebuild

> Construye Containerfiles e imágenes personalizadas basadas en tu `recipe.yml`.
> Más información: <https://github.com/blue-build/cli#how-to-use>.

- Construye una receta:

`bluebuild build {{ruta/a/receta.yml}}`

- Valida una receta:

`bluebuild validate {{ruta/a/receta.yml}}`

- Genera un archivo contenedor:

`bluebuild generate --output {{archivo_contenedor}} {{ruta/a/receta.yml}}`

- Genera una ISO a partir de una receta:

`bluebuild generate-iso --output-dir {{ruta/a/directorio_salida}} --iso-name {{nombre_iso.iso}} recipe {{ruta/a/receta.yml}}`

- Muestra la ayuda:

`bluebuild --help`
