# az bicep

> Gruppo di comandi CLI Bicep.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/bicep>.

- Installa Bicep CLI:

`az bicep install`

- Compila un file Bicep:

`az bicep build {{[-f|--file]}} {{percorso/del/file.bicep}}`

- Tenta di decompilare un file template ARM in un file Bicep:

`az bicep decompile {{[-f|--file]}} {{percorso/del/template_file.json}}`

- Aggiorna Bicep CLI all'ultima versione:

`az bicep upgrade`

- Mostra la versione installata di Bicep CLI:

`az bicep version`

- Elenca tutte le versioni disponibili di Bicep CLI:

`az bicep list-versions`

- Disinstalla Bicep CLI:

`az bicep uninstall`
