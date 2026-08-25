# dnf group

> Gestisce collezioni virtuali di pacchetti su sistemi basati su Fedora.
> Maggiori informazioni: <https://dnf.readthedocs.io/en/latest/command_ref.html#group-command>.

- Elenca i gruppi DNF, mostrando lo stato di installato e non installato in una tabella:

`dnf {{[grp|group]}} list`

- Mostra le informazioni del gruppo DNF, inclusi repository e pacchetti opzionali:

`dnf {{[grp|group]}} info {{group_name}}`

- Installa un gruppo DNF:

`dnf {{[grp|group]}} install {{group_name}}`

- Rimuove un gruppo DNF:

`dnf {{[grp|group]}} remove {{group_name}}`

- Aggiorna un gruppo DNF:

`dnf {{[grp|group]}} upgrade {{group_name}}`
