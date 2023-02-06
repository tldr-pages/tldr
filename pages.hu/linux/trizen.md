# trizen

> Arch Linux segédprogram az Arch User Repository (AUR) csomagok összeállításához. További információ: <https://github.com/trizen/trizen>.

- Az összes AUR csomag szinkronizálása és frissítése:

`trizen -Syua`

- Új csomag telepítése:

`trizen -S {{package}}`

- Egy csomag és függőségeinek eltávolítása:

`trizen -Rs {{package}}`

- Keresés a csomagadatbázisban egy kulcsszóra:

`trizen -Ss {{keyword}}`

- Információk megjelenítése egy csomagról:

`trizen -Si {{package}}`

- Telepített csomagok és verziók listázása:

`trizen -Qe`
