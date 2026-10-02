# pkgctl repo

> Gestisce repository Git di pacchetti e la loro configurazione per Arch Linux.
> Vedi anche: `pkgctl`.
> Maggiori informazioni: <https://manned.org/pkgctl-repo>.

- Clona un repository di pacchetti (richiede l'impostazione di una chiave SSH nell'account GitLab di Arch Linux):

`pkgctl repo clone {{nome_pkg}}`

- Clona un repository di pacchetti tramite HTTPS:

`pkgctl repo clone --protocol https {{nome_pkg}}`

- Crea un nuovo repository di pacchetti GitLab e lo clona dopo la creazione (richiede autenticazione API GitLab valida):

`pkgctl repo create {{pkgbase}}`

- Cambia un repository di pacchetti a una versione specificata:

`pkgctl repo switch {{versione}} {{pkgbase}}`

- Apre il sito web di un repository di pacchetti:

`pkgctl repo web {{pkgbase}}`
