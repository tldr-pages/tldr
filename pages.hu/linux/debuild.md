# debuild

> Eszköz egy Debian csomag forrásból történő összeállításához. További információ: <https://manpages.debian.org/debuild>.

- A csomag összeállítása az aktuális könyvtárban:

`debuild`

- Csak bináris csomagot épít:

`debuild -b`

- A csomag építése után ne futtassa a lintian-t:

`debuild --no-lintian`
