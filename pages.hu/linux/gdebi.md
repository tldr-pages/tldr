# gdebi

> Egyszerű eszköz a `.deb` fájlok telepítéséhez. További információ: <https://www.commandlinux.com/man-page/man1/gdebi.1.html>.

- Helyi `.deb` csomagok telepítése a függőségek feloldásával és telepítésével:

`gdebi {{path/to/package.deb}}`

- A program verziójának megjelenítése:

`gdebi --version`

- Nem jeleníti meg az előrehaladási információkat:

`gdebi {{path/to/package.deb}} --quiet`

- Állítson be egy APT konfigurációs opciót:

`gdebi {{path/to/package.deb}} --option={{APT_OPTS}}`

- Alternatív root dir használata:

`gdebi {{path/to/package.deb}} --root={{path/to/root_dir}}`
