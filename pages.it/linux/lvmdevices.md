# lvmdevices

> Gestisce il file dei dispositivi LVM che elenca i dispositivi di blocco consentiti per i volumi fisici.
> Maggiori informazioni: <https://manned.org/lvmdevices>.

- Elenca i dispositivi registrati nel file dei dispositivi:

`sudo lvmdevices`

- Aggiunge un dispositivo al file dei dispositivi:

`sudo lvmdevices --adddev {{/dev/sdXN}}`

- Rimuove un dispositivo dal file dei dispositivi:

`sudo lvmdevices --deldev {{/dev/sdXN}}`

- Aggiunge un volume fisico tramite il suo PVID:

`sudo lvmdevices --addpvid {{PVID}}`

- Rimuove un volume fisico tramite il suo PVID:

`sudo lvmdevices --delpvid {{PVID}}`

- Aggiorna il file dei dispositivi dopo il cambio di nomi dei dispositivi:

`sudo lvmdevices --update`

- Controlla il file dei dispositivi per problemi:

`sudo lvmdevices --check`

- Visualizza la versione:

`lvmdevices --version`
