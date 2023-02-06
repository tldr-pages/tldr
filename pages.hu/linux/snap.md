# snap

> Eszköz a "snap" önálló szoftvercsomagok kezelésére. Hasonlóan ahhoz, amit a `apt` a ".deb" számára. További információ: <https://manned.org/snap>.

- Egy csomag keresése:

`snap find {{package_name}}`

- Egy csomag telepítése:

`snap install {{package_name}}`

- Egy csomag frissítése:

`snap refresh {{package_name}}`

- Egy csomag frissítése egy másik csatornába (track, risk vagy branch):

`snap refresh {{package_name}} --channel={{channel}}`

- Az összes csomag frissítése:

`snap refresh`

- Alapvető információk megjelenítése a telepített snap szoftverekről:

`snap list`

- Egy csomag eltávolítása:

`snap remove {{package_name}}`

- A rendszerben nemrégiben végrehajtott snap-változások ellenőrzése:

`snap changes`
