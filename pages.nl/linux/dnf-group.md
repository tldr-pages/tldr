# dnf group

> Beheer virtuele collecties van pakketten op Fedora gebaseerde systemen.
> Meer informatie: <https://dnf.readthedocs.io/en/latest/command_ref.html#group-command>.

- Maak een lijst van DNF-groepen, met geïnstalleerde en verwijderde status in een tabel:

`dnf {{[grp|group]}} list`

- Toon DNF groepsinformatie, inclusief repository en optionele pakketten:

`dnf {{[grp|group]}} info {{groepsnaam}}`

- Installeer een DNF groep:

`dnf {{[grp|group]}} install {{groepsnaam}}`

- Verwijder een DNF groep:

`dnf {{[grp|group]}} remove {{groepsnaam}}`

- Upgrade een DNF groep:

`dnf {{[grp|group]}} upgrade {{groepsnaam}}`
