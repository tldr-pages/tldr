# eget

> Könnyedén telepítheti az előre elkészített binárisokat a GitHubról. További információ: <https://github.com/zyedidia/eget>.

- Töltsön le egy előre elkészített bináris változatot az aktuális rendszerhez a GitHub egyik tárolójából:

`eget {{zyedidia/micro}}`

- Letöltés egy URL-címről:

`eget {{https://go.dev/dl/go1.17.5.linux-amd64.tar.gz}}`

- Adja meg a letöltött fájlok helyét:

`eget {{zyedidia/micro}} --to={{path/to/directory}}`

- A `git` címke megadása a legfrissebb verzió használata helyett:

`eget {{zyedidia/micro}} --tag={{v2.0.10}}`

- A legújabb stabil verzió helyett a legfrissebb előverzió telepítése:

`eget {{zyedidia/micro}} --pre-release`

- Csak az eszköz letöltése, az extrahálás kihagyása:

`eget {{zyedidia/micro}} --download-only`

- Csak akkor töltse le, ha van az aktuálisan letöltött verziónál újabb kiadás:

`eget {{zyedidia/micro}} --upgrade-only`
