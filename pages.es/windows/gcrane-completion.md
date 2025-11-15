# gcrane completion

> Generar el script de autocompletado para gcrane para el shell especificado.
> Los shells disponibles son `bash`, `fish`, `powershell` y `zsh`.
> Más información: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Generar el script de autocompletado para tu shell:

`gcrane completion {{nombre_del_shell}}`

- Deshabilitar descripciones de autocompletado:

`gcrane completion {{nombre_del_shell}} --no-descriptions`

- Cargar completaciones en tu sesión actual de shell (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- Cargar completaciones para cada nueva sesión (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- Mostrar ayuda:

`gcrane completion {{nombre_del_shell}} {{[-h|--help]}}`
