# apx

> Csomagkezelő segédprogram a Vanilla OS-hez. Csomagokat telepít a kezelt konténerekbe több forrásból (`apx` támogatja a --aur,--dnf flageket minden parancsban). További információ: <https://github.com/Vanilla-OS/apx>.

- A konténer inicializálása:

`apx init`

- Bizonyos csomagok telepítése a konténerbe:

`apx install {{package1 package2 ...}}`

- Bizonyos csomagok eltávolítása a konténerből:

`apx remove {{package1 package2 ...}}`

- Konkrét csomagok keresése:

`apx search {{package1 package2 ...}}`

- Belépés a kezelt konténer héjába a parancsok végrehajtásához (a konténerből való kilépéshez írja be a `exit` parancsot):

`apx enter`

- A konténerben elérhető csomagok listájának frissítése:

`apx update`

- A konténerben lévő összes telepített csomag frissítése a legújabb elérhető verzióra:

`apx upgrade`
