# toolbox rmi

> Rimuovi immagini Toolbx.
> Vedi anche: `toolbox rm`.
> Maggiori informazioni: <https://manned.org/toolbox-rmi>.

- Rimuovi una o più immagini Toolbx:

`toolbox rmi {{nome_immagine1 nome_immagine2 ...}}`

- Rimuovi tutte le immagini Toolbx:

`toolbox rmi {{[-a|--all]}}`

- Forza la rimozione di un'immagine Toolbx attualmente in uso da un contenitore (il contenitore verrà rimosso anch'esso):

`toolbox rmi {{[-f|--force]}} {{nome_immagine}}`
