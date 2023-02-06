# xdg-desktop-menu

> Parancssori eszköz az asztali menüelemek telepítéséhez vagy eltávolításához. További információ: <https://manned.org/xdg-desktop-menu>.

- Alkalmazás telepítése az asztali menürendszerbe:

`xdg-desktop-menu install {{path/to/file.desktop}}`

- Alkalmazás telepítése az asztali menürendszerbe úgy, hogy a gyártó előtag ellenőrzése ki van kapcsolva:

`xdg-desktop-menu install --novendor {{path/to/file.desktop}}`

- Alkalmazás eltávolítása az asztali menürendszerből:

`xdg-desktop-menu uninstall {{path/to/file.desktop}}`

- Az asztali menürendszer frissítésének kikényszerítése:

`xdg-desktop-menu forceupdate --mode {{user|system}}`
