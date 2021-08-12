# loc

> Instrument scris în Rust care contorizează liniile de cod.
> Mai multe informaţii: <https://github.com/cgag/loc>

- Tipăriți linii de cod în directorul curent:

`loc`

- Tipăriți linii de cod în directorul țintă:

`loc {{path/to/directory}}`

- Tipăriți linii de cod cu statistici pentru fișiere individuale:

`loc --files`

- Tipăriți linii de cod fără fișiere.gitignore (etc.) (de exemplu, două steaguri -u vor conta suplimentar fișiere ascunse și dirs):

`loc -u`
