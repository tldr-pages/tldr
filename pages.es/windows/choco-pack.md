# choco pack

> Empaqueta una especificación de NuGet en un archivo `.nupkg`.
> Más información: <https://docs.chocolatey.org/en-us/create/commands/pack/>.

- Empaqueta una especificación de NuGet en un archivo `.nupkg`:

`choco pack {{ruta\al\archivo_especificacion}}`

- Empaqueta una especificación de NuGet especificando la versión del archivo resultante:

`choco pack {{ruta\al\archivo_especificacion}} --version {{versión}}`

- Empaqueta una especificación de NuGet en un directorio específico:

`choco pack {{ruta\al\archivo_especificacion}} {{[--out|--output-directory]}} {{ruta\al\directorio_salida}}`
