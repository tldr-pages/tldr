# zypper

> SUSE és openSUSE csomagkezelő segédprogram. Más csomagkezelőkben használt, ezzel egyenértékű parancsokért lásd: https: [//wiki.archlinux.org/title/Pacman/Rosetta. További](https://wiki.archlinux.org/title/Pacman/Rosetta) információ: <https://en.opensuse.org/SDB:Zypper_manual>.

- Az elérhető csomagok és verziók listájának szinkronizálása:

`zypper refresh`

- Új csomag telepítése:

`zypper install {{package}}`

- Egy csomag eltávolítása:

`zypper remove {{package}}`

- A telepített csomagok frissítése a legújabb elérhető verziókra:

`zypper update`

- Csomag keresése kulcsszó alapján:

`zypper search {{keyword}}`

- A konfigurált tárolókkal kapcsolatos információk megjelenítése:

`zypper repos --sort-by-priority`
