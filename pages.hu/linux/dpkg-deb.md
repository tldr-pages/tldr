# dpkg-deb

> Csomagolás, kicsomagolás és információszolgáltatás a Debian archívumokról. További információ: <https://manpages.debian.org/latest/dpkg/dpkg-deb.html>.

- Információk megjelenítése egy csomagról:

`dpkg-deb --info {{path/to/file.deb}}`

- A csomag nevének és verziójának megjelenítése egy sorban:

`dpkg-deb --show {{path/to/file.deb}}`

- A csomag tartalmának felsorolása:

`dpkg-deb --contents {{path/to/file.deb}}`

- A csomag tartalmának egy könyvtárba történő kicsomagolása:

`dpkg-deb --extract {{path/to/file.deb}} {{path/to/directory}}`

- Csomag létrehozása egy megadott könyvtárból:

`dpkg-deb --build {{path/to/directory}}`
