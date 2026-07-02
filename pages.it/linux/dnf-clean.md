# dnf clean

> Esegue la pulizia dei file temporanei mantenuti per i repository basati su Red Hat.
> Maggiori informazioni: <https://dnf.readthedocs.io/en/latest/command_ref.html#clean-command>.

- Rimuove i file cache generati dai metadati del repository:

`dnf clean dbcache`

- Marca i metadati del repository come scaduti:

`dnf clean expire-cache`

- Rimuove i metadati del repository:

`dnf clean metadata`

- Rimuove qualsiasi pacchetto in cache dal sistema:

`dnf clean packages`

- Pulisce tutti i metadati specifici del repository DNF e i file in cache (tutti i precedenti):

`dnf clean all`
