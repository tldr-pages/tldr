# choco pack

> Empaqueta una especificación de NuGet en un archivo `nupkg`.
> Más información: <https://chocolatey.org/docs/commands-pack>.

- Empaquetar una especificación de NuGet en un archivo `nupkg`:

`choco pack {{ruta\al\archivo_especificacion}}`

- Empaquetar una especificación de NuGet especificando la versión del archivo resultante:

`choco pack {{ruta\al\archivo_especificacion}} --version {{versión}}`

- Empaquetar una especificación de NuGet en un directorio específico:

`choco pack {{ruta\al\archivo_especificacion}} --output-directory {{ruta\al\directorio_salida}}`
