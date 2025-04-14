# wsl

> Gestisce WSL (Windows Subsystem for Linux).
> Maggiori informazioni: <https://learn.microsoft.com/windows/wsl/reference>.

- Avvia una shell Linux (nella distribuzione predefinita):

`wsl {{comando_shell}}`

- Esegui un comando Linux senza usare shell:

`wsl --exec {{comando}} {{agomenti_del_comando}}`

- Specifica una distribuzione particolare:

`wsl --distribution {{distribuzione}} {{shell_command}}`

- Elenca distribuzioni disponibili:

`wsl --list`

- Esporta una distribuzione su file `.tar`:

`wsl --export {{distribuzione}} {{percorso\al\file_della_distribuzione.tar}}`

- Importa una distribuzione da file `.tar`:

`wsl --import {{distribuzione}} {{percorso\alla\cartella_di_installazione}} {{percorso\al\file_della_distribuzione.tar}}`

- Modifica la versione di wsl da usare per la distribuzione specificata:

`wsl --set-version {{distribuzione}} {{versione}}`

- Arresta WSL:

`wsl --shutdown`