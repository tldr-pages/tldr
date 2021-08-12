# borg

> Eliminarea duplicatelor instrumentului de backup.
> Creează copii de rezervă locale sau la distanță care pot fi montate ca sisteme de fișiere.
> Mai multe informaţii: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>

- Iniţializarea unui depozit (local):

`borg init {{path/to/repo_directory}}`

- Copierea de rezervă a unui director în depozit, creând o arhivă numită „Luni”:

`borg create --progress {{path/to/repo_directory}}::{{Monday}} {{path/to/source_directory}}`

- Listează toate arhivele dintr-un depozit:

`borg list {{path/to/repo_directory}}`

- Extrageți un anumit director din arhiva „Luni” într-un depozit la distanță, excluzând toate fișierele `*.ext`:

`borg extract {{user}}@{{host}}:{{path/to/repo_directory}}::{{Monday}} {{path/to/target_directory}} --exclude '{{*.ext}}'`

- Îndepărtați un depozit ștergând toate arhivele mai vechi de 7 zile, listând modificările:

`borg prune --keep-within {{7d}} --list {{path/to/repo_directory}}`

- Montați un depozit ca sistem de fișiere FUSE:

`borg mount {{path/to/repo_directory}}::{{Monday}} {{path/to/mountpoint}}`

- Afișați ajutorul pentru crearea de arhive:

`borg create --help`
