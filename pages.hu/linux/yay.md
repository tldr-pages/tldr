# yay

> Még egy joghurt: `pacman` További információ: <https://github.com/Jguer/yay>.

- Interaktívan keres és telepít csomagokat a repos-ból és az AUR-ból:

`yay {{package_name|search_term}}`

- Szinkronizálja és frissíti az összes csomagot a repos-ból és az AUR-ból:

`yay`

- Csak az AUR csomagok szinkronizálása és frissítése:

`yay -Sua`

- Új csomag telepítése a repos-ból és az AUR-ból:

`yay -S {{package_name}}`

- Telepített csomag és függőségei, valamint konfigurációs fájljai eltávolítása:

`yay -Rns {{package_name}}`

- Keresés a csomagadatbázisban egy kulcsszóra a repos-ból és az AUR-ból:

`yay -Ss {{keyword}}`

- Árva csomagok eltávolítása (függőségként telepített, de egyetlen csomag által sem igényelt csomagok):

`yay -Yc`

- A telepített csomagok és a rendszer állapotára vonatkozó statisztikák megjelenítése:

`yay -Ps`
