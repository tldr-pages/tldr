# toolbox

> Gestisci ambienti a riga di comando containerizzati su Linux.
> Alcuni sottocomandi come `create` hanno la propria documentazione d'uso.
> Maggiori informazioni: <https://manned.org/toolbox>.

- Entra in un contenitore Toolbx per usarlo interattivamente:

`toolbox enter {{contenitore}}`

- Rimuovi uno o più contenitori:

`toolbox rm {{contenitore1 contenitore2 ...}}`

- Rimuovi una o più immagini:

`toolbox rmi {{immagine1 immagine2 ...}}`

- Mostra l'aiuto per un sottocomando specifico (come `create`, `enter`, `rm`, ecc.):

`toolbox help {{sottocomando}}`

- Mostra aiuto:

`toolbox {{[-h|--help]}}`

- Mostra versione:

`toolbox --version`
