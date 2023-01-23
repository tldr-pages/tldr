# pacaur

> Arch Linuxhoz készült segédprogram az Arch User Repositoryból származó csomagok összeállításához és telepítéséhez. További információ: <https://github.com/rmarquis/pacaur>.

- Az összes csomag szinkronizálása és frissítése (tartalmazza az AUR-t is):

`pacaur -Syu`

- Csak az AUR csomagok szinkronizálása és frissítése:

`pacaur -Syua`

- Új csomag telepítése (tartalmazza az AUR-t):

`pacaur -S {{package_name}}`

- Egy csomag és függőségeinek eltávolítása (tartalmazza az AUR csomagokat):

`pacaur -Rs {{package_name}}`

- Keresés a csomagadatbázisban egy kulcsszóra (az AUR-t is beleértve):

`pacaur -Ss {{keyword}}`

- Az összes jelenleg telepített csomag listázása (AUR-csomagokat is beleértve):

`pacaur -Qs`
