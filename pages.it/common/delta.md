# delta

> Visualizzatore per output Git e diff.
> Maggiori informazioni: <https://dandavison.github.io/delta/full---help-output.html>[attached_file:1].

- Confronta file o directory:

`delta {{percorso/del/vecchio_file_o_directory}} {{percorso/del/nuovo_file_o_directory}}`

- Confronta file o directory, mostrando i numeri di riga:

`delta {{[-n|--line-numbers]}} {{percorso/del/vecchio_file_o_directory}} {{percorso/del/nuovo_file_o_directory}}`

- Confronta file o directory, mostrando le differenze affiancate:

`delta {{[-s|--side-by-side]}} {{percorso/del/vecchio_file_o_directory}} {{percorso/del/nuovo_file_o_directory}}`

- Confronta file o directory, ignorando le impostazioni di configurazione Git:

`delta --no-gitconfig {{percorso/del/vecchio_file_o_directory}} {{percorso/del/nuovo_file_o_directory}}`

- Confronta, rendendo hash commit, nomi file e numeri di riga come collegamenti ipertestuali secondo la specifica per emulatori terminal:

`delta --hyperlinks {{percorso/del/vecchio_file_o_directory}} {{percorso/del/nuovo_file_o_directory}}`

- Visualizza le impostazioni correnti:

`delta --show-config`

- Visualizza i linguaggi supportati e le estensioni di file associate:

`delta --list-languages`
