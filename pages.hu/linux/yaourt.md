# yaourt

> Arch Linux segédprogram az Arch User Repositoryból történő csomagépítéshez. További információ: <https://linuxcommandlibrary.com/man/yaourt>.

- Az összes csomag szinkronizálása és frissítése (beleértve az AUR-t is):

`yaourt -Syua`

- Új csomag telepítése (beleértve az AUR-t is):

`yaourt -S {{package_name}}`

- Egy csomag és függőségeinek eltávolítása (beleértve az AUR csomagokat):

`yaourt -Rs {{package_name}}`

- Keresés a csomagadatbázisban egy kulcsszóra (beleértve az AUR csomagokat is):

`yaourt -Ss {{package_name}}`

- A telepített csomagok, verziók és tárolók listázása (az AUR csomagok a "local" tároló neve alatt lesznek felsorolva):

`yaourt -Q`
