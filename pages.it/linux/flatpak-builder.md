# flatpak-builder

> Aiuta a compilare le dipendenze delle applicazioni.
> Maggiori informazioni: <https://docs.flatpak.org/en/latest/flatpak-builder-command-reference.html>.

- Compila un Flatpak e lo esporta in un nuovo repository:

`flatpak-builder {{path/to/build_directory}} {{path/to/manifest}}`

- Compila un Flatpak e lo esporta nel repository specificato:

`flatpak-builder --repo {{repository_name}} {{path/to/build_directory}} {{path/to/manifest}}`

- Compila un Flatpak e lo installa localmente:

`flatpak-builder --install {{path/to/build_directory}} {{path/to/manifest}}`

- Compila e firma un Flatpak e lo esporta nel repository specificato:

`flatpak-builder --gpg-sign {{key_id}} --repo {{repository_name}} {{path/to/manifest}}`

- Esegue una shell all'interno di un sandbox dell'applicazione senza installarla:

`flatpak-builder --run {{path/to/build_directory}} {{path/to/manifest}} {{sh}}`
