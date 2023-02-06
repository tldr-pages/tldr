# restic

> Gyors, biztonságos és hatékony biztonsági mentőprogram. További információ: <https://restic.net>.

- Egy biztonsági mentési adattár inicializálása a megadott helyi könyvtárban:

`restic init --repo {{path/to/repository}}`

- Egy könyvtár biztonsági mentése az adattárba:

`restic --repo {{path/to/repository}} backup {{path/to/directory}}`

- Az adattárban jelenleg tárolt biztonsági mentések pillanatfelvételeinek megjelenítése:

`restic --repo {{path/to/repository}} snapshots`

- Egy adott biztonsági mentési pillanatkép visszaállítása egy célkönyvtárba:

`restic --repo {{path/to/repository}} restore {{latest|snapshot_id}} --target {{path/to/target}}`

- Egy adott útvonal visszaállítása egy adott biztonsági mentésből egy célkönyvtárba:

`restic --repo {{path/to/repository}} restore {{snapshot_id}} --target {{path/to/target}} --include {{path/to/restore}}`

- Az adattár megtisztítása, és csak a legfrissebb pillanatfelvétel megtartása minden egyes egyedi biztonsági másolatról:

`restic forget --keep-last 1 --prune`
