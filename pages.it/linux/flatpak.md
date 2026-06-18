# flatpak

> Compila, installa ed esegue applicazioni flatpak e runtime.
> Maggiori informazioni: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- Esegue un'applicazione installata:

`flatpak run {{com.example.app}}`

- Installa un'applicazione da una fonte remota:

`flatpak install {{remote_name}} {{com.example.app}}`

- Elenca le applicazioni installate, ignorando i runtime:

`flatpak list --app`

- Aggiorna tutte le applicazioni e i runtime installati:

`flatpak update`

- Aggiunge una fonte remota:

`flatpak remote-add --if-not-exists {{remote_name}} {{remote_url}}`

- Rimuove un'applicazione installata:

`flatpak remove {{com.example.app}}`

- Rimuove tutte le applicazioni inutilizzate:

`flatpak remove --unused`

- Mostra informazioni su un'applicazione installata:

`flatpak info {{com.example.app}}`
