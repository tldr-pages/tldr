# aptitude

> Debian és Ubuntu csomagkezelő segédprogram. További információ: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Az elérhető csomagok és verziók listájának szinkronizálása. Ezt kell először futtatni, mielőtt a további aptitude parancsokat futtatnánk:

`aptitude update`

- Új csomag és függőségeinek telepítése:

`aptitude install {{package}}`

- Egy csomag keresése:

`aptitude search {{package}}`

- Egy telepített csomag keresése (`?installed` egy aptitude kereső kifejezés):

`aptitude search '?installed({{package}})'`

- Egy csomag és a tőle függő összes csomag eltávolítása:

`aptitude remove {{package}}`

- A telepített csomagok frissítése a legújabb elérhető verziókra:

`aptitude upgrade`

- Telepített csomagok frissítése (mint a `aptitude upgrade`), beleértve az elavult csomagok eltávolítását és további csomagok telepítését az új csomagfüggőségek kielégítésére:

`aptitude full-upgrade`

- Egy telepített csomagot várakoztathat, hogy megakadályozza az automatikus frissítést:

`aptitude hold '?installed({{package}})'`
