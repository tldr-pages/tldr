# lsusb

> Mostra informació sobre ports i dispositius USB.
> Més informació: <https://manned.org/lsusb>.

- Llista tots els dispositius USB disponibles:

`lsusb`

- Llista la jerarquia de dispositius USB en forma d'arbre:

`lsusb -t`

- Llista tots els disposititus USB de forma verbosa:

`lsusb --verbose`

- Llista informació detallada sobre un dispositiu USB determinat:

`lsusb -D {{dispositiu}}`

- Llista només dispositius amb un ID d'assemblador i producte determinat:

`lsusb -d {{assemblador}}:{{producte}}`
