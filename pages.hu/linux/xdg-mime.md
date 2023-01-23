# xdg-mime

> MIME típusok lekérdezése és kezelése az XDG szabvány szerint. További információ: <https://portland.freedesktop.org/doc/xdg-mime.html>.

- Egy fájl MIME-típusának megjelenítése:

`xdg-mime query filetype {{path/to/file}}`

- A PNG-k megnyitásához használt alapértelmezett alkalmazás megjelenítése:

`xdg-mime query default {{image/png}}`

- Egy adott fájl megnyitásához használt alapértelmezett alkalmazás megjelenítése:

`xdg-mime query default $(xdg-mime query filetype {{path/to/file}})`

- Az imv beállítása alapértelmezett alkalmazásként a PNG és JPEG képek megnyitásához:

`xdg-mime default {{imv.desktop}} {{image/png}} {{image/jpeg}}`
