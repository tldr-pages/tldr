# spi

> Egy meta csomagkezelő, amely csomagokat és slackbuildeket is kezel. További információ: <https://github.com/gapan/spi>.

- Az elérhető csomagok és slackbuildek listájának frissítése:

`spi --update`

- Csomag vagy slackbuild telepítése:

`spi --install {{package/slackbuild_name}}`

- Az összes telepített csomag frissítése az elérhető legújabb verziókra:

`spi --upgrade`

- Csomagok vagy slackbuildek keresése a csomag neve vagy leírása alapján:

`spi {{search_terms}}`

- Információk megjelenítése egy csomagról vagy slackbuildről:

`spi --show {{package/slackbuild_name}}`

- A helyi csomag- és slackbuild-cache-ek törlése:

`spi --clean`
