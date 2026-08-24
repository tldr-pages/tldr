# dnf

> Gestore di pacchetti per Fedora 41+ e RHEL 10.
> Per comandi equivalenti in altri gestori di pacchetti, vedi <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Maggiori informazioni: <https://dnf5.readthedocs.io/en/latest/commands/index.html>.

- Aggiorna i pacchetti installati alle versioni più recenti disponibili:

`sudo dnf {{[up|upgrade]}}`

- Cerca pacchetti tramite parole chiave:

`dnf {{[se|search]}} {{keyword1 keyword2 ...}}`

- Mostra i dettagli di un pacchetto:

`dnf {{[if|info]}} {{package}}`

- Installa nuovi pacchetti (usa `--assumeyes` per confermare automaticamente tutte le richieste):

`sudo dnf {{[in|install]}} {{package1 package2 ...}}`

- Rimuove pacchetti:

`sudo dnf {{[rm|remove]}} {{package1 package2 ...}}`

- Elenca i pacchetti installati:

`dnf {{[ls|list]}} --installed`

- Trova quali pacchetti forniscono un dato comando:

`dnf provides {{command}}`

- Pulisce i dati in cache:

`sudo dnf clean {{all|dbcache|expire-cache|metadata|packages}}`
