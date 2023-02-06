# borg

> Deduplikáló mentőeszköz. Helyi vagy távoli mentéseket készít, amelyek fájlrendszerként csatlakoztathatók. További információ: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- (Helyi) adattár inicializálása:

`borg init {{path/to/repo_directory}}`

- Biztonsági mentés egy könyvtárról az adattárba, létrehozva egy "Monday" nevű archívumot:

`borg create --progress {{path/to/repo_directory}}::{{Monday}} {{path/to/source_directory}}`

- Az összes archívum listázása egy adattárban:

`borg list {{path/to/repo_directory}}`

- Egy távoli adattárban lévő "Monday" archívumból egy adott könyvtár kivonása, az összes `*.ext` fájl kizárásával:

`borg extract {{user}}@{{host}}:{{path/to/repo_directory}}::{{Monday}} {{path/to/target_directory}} --exclude '{{*.ext}}'`

- Egy adattár metszése a 7 napnál régebbi archívumok törlésével, a változások listázása:

`borg prune --keep-within {{7d}} --list {{path/to/repo_directory}}`

- Adattár FUSE fájlrendszerként történő csatlakoztatása:

`borg mount {{path/to/repo_directory}}::{{Monday}} {{path/to/mountpoint}}`

- Súgó megjelenítése az archívumok létrehozásához:

`borg create --help`
