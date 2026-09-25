# gcrane completion

> Genera el script de autocompletado para gcrane para el intérprete de comandos especificado.
> Los intérpretes de comandos disponibles son `bash`, `fish`, `powershell` y `zsh`.
> Más información: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Genera el script de autocompletado para tu intérprete de comandos:

`gcrane completion {{nombre_del_intérprete_de_comandos}}`

- Deshabilita descripciones de autocompletado:

`gcrane completion {{nombre_del_intérprete_de_comandos}} --no-descriptions`

- Carga autocompletados en tu sesión actual de intérpretes de comandos (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- Carga autocompletados para cada nueva sesión (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- Muestra la ayuda:

`gcrane completion {{nombre_del_intérprete_de_comandos}} {{[-h|--help]}}`
