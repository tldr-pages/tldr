# flatpak

> Construi, instalați și executați aplicații flatpak și runtime.
> Mai multe informaţii: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>

- Rulați o aplicație instalată:

`flatpak run {{name}}`

- Instalați o aplicație dintr-o sursă de la distanță:

`flatpak install {{remote}} {{name}}`

- Listează toate aplicațiile instalate și runtime:

`flatpak list`

- Actualizați toate aplicațiile instalate și runtime:

`flatpak update`

- Adăugați o sursă de la distanță:

`flatpak remote-add --if-not-exists {{remote_name}} {{remote_url}}`

- Listează toate sursele de la distanță configurate:

`flatpak remote-list`

- Eliminați o aplicație instalată:

`flatpak remove {{name}}`

- Afișați informații despre o aplicație instalată:

`flatpak info {{name}}`
