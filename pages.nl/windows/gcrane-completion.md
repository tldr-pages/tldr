# gcrane completion

> Genereer het autocompletion script voor gcrane voor de opgegeven shell.
> De beschikbare shells zijn `bash`, `fish`, `powershell` en `zsh`.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Genereer het autocompletion script voor je shell:

`gcrane completion {{shell_naam}}`

- Zet de completion beschrijvingen uit:

`gcrane completion {{shell_naam}} --no-descriptions`

- Laad completions in je huidige shellsessie (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- Laad completions voor elke nieuwe sessie (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- Toon de help:

`gcrane completion {{shell_naam}} {{[-h|--help]}}`
