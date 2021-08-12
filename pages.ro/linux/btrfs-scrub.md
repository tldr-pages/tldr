# btrfs scrub

> Scrub sisteme de fișiere btrfs pentru a verifica integritatea datelor.
> Se recomandă să rulați o freză o dată pe lună.
> Mai multe informaţii: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-scrub>

- Începe un exfoliant:

`sudo btrfs scrub start {{path/to/btrfs_mount}}`

- Afișați starea unui exfoliant în curs de desfășurare sau ultima completare:

`sudo btrfs scrub status {{path/to/btrfs_mount}}`

- Anulează un exfoliant continuu:

`sudo btrfs scrub cancel {{path/to/btrfs_mount}}`

- Reluați o freză anulată anterior:

`sudo btrfs scrub resume {{path/to/btrfs_mount}}`

- Începeți o freză, dar așteptați până când frecarea se termină înainte de a ieși:

`sudo btrfs scrub start -B {{path/to/btrfs_mount}}`

- Porniți o frecare în modul silențios (nu imprimă erori sau statistici):

`sudo btrfs scrub start -q {{path/to/btrfs_mount}}`
