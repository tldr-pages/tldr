# flatpak remote-info

> Mostra informazioni su un'applicazione o un runtime in un remoto.
> Maggiori informazioni: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remote-info>.

- Mostra informazioni su un flatpak:

`flatpak remote-info {{remote_name}} {{com.example.app}}`

- Mostra un registro delle versioni precedenti in un remoto:

`flatpak remote-info --log {{remote_name}} {{com.example.app}}`

- Mostra informazioni su un commit specifico, invece che sull'ultima versione:

`flatpak remote-info --commit {{COMMIT}} {{remote_name}} {{com.example.app}}`
