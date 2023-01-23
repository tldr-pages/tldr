# localectl

> A rendszerváltozat és a billentyűzetkiosztás beállításainak vezérlése. További információ: <https://www.freedesktop.org/software/systemd/man/localectl.html>.

- A rendszerváltozat és a billentyűzetkiosztás aktuális beállításainak megjelenítése:

`localectl`

- Az elérhető helyi beállítások listája:

`localectl list-locales`

- Rendszerhelyszínváltozó beállítása:

`localectl set-locale {{LANG}}={{en_US.UTF-8}}`

- Az elérhető billentyűzetleképezések listázása:

`localectl list-keymaps`

- A konzol és az X11 rendszerbillentyűzet-hozzárendelés beállítása:

`localectl set-keymap {{us}}`
