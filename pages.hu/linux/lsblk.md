# lsblk

> Az eszközökre vonatkozó információk listája. További információ: <https://manned.org/lsblk>.

- Az összes tárolóeszköz felsorolása fa-szerű formátumban:

`lsblk`

- Az üres eszközök listázása is:

`lsblk -a`

- A SIZE oszlopot bájtokban írja ki, nem pedig ember által olvasható formátumban:

`lsblk -b`

- Információk kiadása a fájlrendszerekről:

`lsblk -f`

- ASCII karakterek használata a fa formázásához:

`lsblk -i`

- Kimeneti információ a blokk-eszköz topológiáról:

`lsblk -t`

- A fő eszközszámok vesszővel elválasztott listájában megadott eszközök kizárása:

`lsblk -e {{1,7}}`

- Egyéni összefoglaló megjelenítése az oszlopok vesszővel elválasztott listájával:

`lsblk --output {{NAME}},{{SERIAL}},{{MODEL}},{{TRAN}},{{TYPE}},{{SIZE}},{{FSTYPE}},{{MOUNTPOINT}}`
