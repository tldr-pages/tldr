# cryptsetup

> Kezelheti a sima dm-crypt és a LUKS (Linux Unified Key Setup) titkosított köteteket. További információk: <https://gitlab.com/cryptsetup/cryptsetup/>.

- LUKS kötet inicializálása (felülírja a partíció összes adatát):

`cryptsetup luksFormat {{/dev/sda1}}`

- Nyisson meg egy LUKS kötetet és hozzon létre egy dekódolt leképezést a `/dev/mapper/{{target}}` címen:

`cryptsetup luksOpen {{/dev/sda1}} {{target}}`

- Meglévő leképezés eltávolítása:

`cryptsetup luksClose {{target}}`

- A LUKS kötet jelszavának módosítása:

`cryptsetup luksChangeKey {{/dev/sda1}}`
