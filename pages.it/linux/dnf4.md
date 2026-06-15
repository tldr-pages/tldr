# dnf4

> Gestore di pacchetti per RHEL 8/9 e versioni precedenti di Fedora (pre-41).
> Per comandi equivalenti in altri gestori di pacchetti, vedi <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Maggiori informazioni: <https://dnf.readthedocs.io/en/latest/command_ref.html>.

- Aggiorna i pacchetti installati alle versioni più recenti disponibili:

`sudo dnf4 {{[up|upgrade]}}`

- Cerca pacchetti tramite parole chiave:

`dnf4 {{[se|search]}} {{keyword1 keyword2 ...}}`

- Mostra i dettagli di un pacchetto:

`dnf4 {{[if|info]}} {{package}}`

- Installa un nuovo pacchetto (usa `--assumeyes` per confermare automaticamente tutte le richieste):

`sudo dnf4 {{[in|install]}} {{package1 package2 ...}}`

- Rimuove un pacchetto:

`sudo dnf4 {{[rm|remove]}} {{package1 package2 ...}}`

- Elenca i pacchetti installati:

`dnf4 {{[ls|list]}} --installed`

- Trova quali pacchetti forniscono un dato comando:

`dnf4 {{[wp|provides]}} {{command}}`

- Visualizza tutte le operazioni passate:

`dnf4 {{[hist|history]}}`
