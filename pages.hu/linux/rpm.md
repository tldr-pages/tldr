# rpm

> RPM csomagkezelő. A más csomagkezelőkben használt egyenértékű parancsokért lásd: https: [//wiki.archlinux.org/title/Pacman/Rosetta. További](https://wiki.archlinux.org/title/Pacman/Rosetta) információ: <https://rpm.org/>.

- A httpd csomag verziójának megjelenítése:

`rpm --query {{httpd}}`

- Az összes megfelelő csomag verzióinak listázása:

`rpm --query --all '{{mariadb*}}'`

- Egy csomag erőszakos telepítése a jelenleg telepített verziókra való tekintet nélkül:

`rpm --upgrade {{package_name.rpm}} --force`

- Egy fájl tulajdonosának azonosítása és a csomag verziójának megjelenítése:

`rpm --query --file {{/etc/postfix/main.cf}}`

- A csomag tulajdonában lévő fájlok listázása:

`rpm --query --list {{kernel}}`

- Szkriptek megjelenítése egy RPM-fájlból:

`rpm --query --package --scripts {{package_name.rpm}}`

- A megfelelő csomagok módosított, hiányzó és/vagy hibásan telepített fájljainak megjelenítése:

`rpm --verify --all '{{php-*}}'`

- Egy adott csomag változásnaplójának megjelenítése:

`rpm --query --changelog {{package_name}}`
