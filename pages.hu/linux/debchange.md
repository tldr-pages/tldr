# debchange

> Eszköz a Debian forráscsomag debian/changelog fájljának karbantartására. További információ: <https://manpages.debian.org/debchange>.

- Új verzió hozzáadása egy nem karbantartó feltöltéséhez a changeloghoz:

`debchange --nmu`

- changelog bejegyzés hozzáadása az aktuális verzióhoz:

`debchange --append`

- changelog bejegyzés hozzáadása a megadott azonosítóval rendelkező hiba lezárásához:

`debchange --closes {{bug_id}}`
