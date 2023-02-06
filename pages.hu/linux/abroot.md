# abroot

> Az ABRoot segédprogram teljes változtathatatlanságot és atomicitást biztosít 2 gyökérpartíció állapota (A⟺B) közötti tranzakciókkal. Emellett lehetővé teszi az on-demand tranzakciókat egy tranzakciós héjon keresztül. További információ: <https://github.com/Vanilla-OS/ABRoot>.

- A jelenlegi vagy jövőbeli gyökérpartíció állapotának kimenete:

`sudo abroot get {{present|future}}`

- Lépjen be a tranzakciós héjba a jövőbeli gyökérpartícióban, és a következő indításkor váltson gyökeret:

`sudo abroot shell`

- Egy adott parancs végrehajtása a tranzakciós héjban a jövőbeli root partícióban, és a következő rendszerindításkor váltás:

`sudo abroot exec "{{command}}"`

- Bizonyos csomagok telepítése a hoszton belül a tranzakciós héjon belül a jövőbeli gyökérpartícióban, és a következő indításkor váltás:

`sudo abroot exec apt install {{package1 package2 ...}}`

- A rendszerindító partíció frissítése (csak haladó felhasználók számára):

`sudo abroot _update-boot`

- Súgó megjelenítése:

`abroot --help`

- Verzió megjelenítése:

`abroot --version`
