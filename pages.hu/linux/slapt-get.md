# slapt-get

> Egy apt-szerű rendszer a Slackware csomagkezeléséhez. A csomagforrásokat a slapt-getrc fájlban kell beállítani. További információ: <https://software.jaos.org>.

- Az elérhető csomagok és verziók listájának frissítése:

`slapt-get --update`

- Telepítsen egy csomagot, vagy frissítse azt a legújabb elérhető verzióra:

`slapt-get --install {{package_name}}`

- Egy csomag eltávolítása:

`slapt-get --remove {{package_name}}`

- Az összes telepített csomag frissítése a legújabb elérhető verzióra:

`slapt-get --upgrade`

- A csomagok keresése a csomag neve, a lemezkészlet vagy a verzió alapján:

`slapt-get --search {{package_name}}`

- Információk megjelenítése egy csomagról:

`slapt-get --show {{package_name}}`
