# distrobox-export

> Esporta app/servizio/binario dal container all'OS host.
> Vedi anche: `distrobox`.
> Maggiori informazioni: <https://distrobox.it/usage/distrobox-export/>.

- Esporta un'app dal container all'host (la voce desktop/icona apparirà nell'elenco delle applicazioni del tuo sistema host):

`distrobox-export {{[-a|--app]}} {{package}} {{[-ef|--extra-flags]}} "--foreground"`

- Esporta un binario dal container all'host:

`distrobox-export {{[-b|--bin]}} {{percorso/del/binary}} {{[-ep|--export-path]}} {{percorso/del/binary_on_host}}`

- Esporta un binario dal container all'host (ad es. `$HOME/.local/bin`):

`distrobox-export {{[-b|--bin]}} {{percorso/del/binary}} {{[-ep|--export-path]}} {{percorso/dell/export}}`

- Esporta un servizio dal container all'host (`--sudo` eseguirà il servizio come root dentro il container):

`distrobox-export --service {{package}} {{[-ef|--extra-flags]}} "--allow-newer-config" {{[-S|--sudo]}}`

- Annulla l'esportazione/elimina un'applicazione esportata:

`distrobox-export {{[-a|--app]}} {{package}} {{[-d|--delete]}}`
