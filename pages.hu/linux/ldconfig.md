# ldconfig

> Symlinkek és gyorsítótár beállítása a megosztott könyvtárfüggőségekhez. További információ: <https://manned.org/ldconfig>.

- A szimlinkek frissítése és a gyorsítótár újraépítése (általában új könyvtár telepítésekor fut):

`sudo ldconfig`

- Egy adott könyvtár szimlinkjeinek frissítése:

`sudo ldconfig -n {{path/to/directory}}`

- Kiírja a könyvtárakat a gyorsítótárban, és ellenőrzi, hogy egy adott könyvtár jelen van-e:

`ldconfig -p | grep {{library_name}}`
