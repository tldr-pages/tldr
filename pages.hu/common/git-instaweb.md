# git instaweb

> Segédprogram a GitWeb szerver indításához. További információ: <https://git-scm.com/docs/git-instaweb>.

- GitWeb szerver indítása az aktuális Git tárolóhoz:

`git instaweb --start`

- Csak a localhost-on figyeljen:

`git instaweb --start --local`

- Figyeljen egy adott porton:

`git instaweb --start --port {{1234}}`

- Megadott HTTP-démon használata:

`git instaweb --start --httpd {{lighttpd|apache2|mongoose|plackup|webrick}}`

- Egy webböngésző automatikus indítása is:

`git instaweb --start --browser`

- A jelenleg futó GitWeb kiszolgáló leállítása:

`git instaweb --stop`

- A jelenleg futó GitWeb kiszolgáló újraindítása:

`git instaweb --restart`
