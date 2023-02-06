# tlmgr

> Kezeli a meglévő TeX Live telepítés csomagjait és konfigurációs beállításait. Néhány alparancsnak, mint például a `tlmgr paper`, saját használati dokumentációja van. További információ: <https://www.tug.org/texlive/tlmgr.html>.

- Egy csomag és függőségeinek telepítése:

`tlmgr install {{package}}`

- Egy csomag és függőségeinek eltávolítása:

`tlmgr remove {{package}}`

- Információk megjelenítése egy csomagról:

`tlmgr info {{package}}`

- Az összes csomag frissítése:

`tlmgr update --all`

- Lehetséges frissítések megjelenítése anélkül, hogy bármit is frissítene:

`tlmgr update --list`

- A tlmgr GUI verziójának elindítása:

`tlmgr gui`

- Az összes TeX Live konfiguráció listázása:

`tlmgr conf`
