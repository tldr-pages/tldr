# bw

> CLI a Bitwarden páncéltermek eléréséhez és kezeléséhez. További információ: <https://help.bitwarden.com/article/cli/>.

- Jelentkezzen be egy Bitwarden felhasználói fiókba:

`bw login`

- Kijelentkezés egy Bitwarden felhasználói fiókból:

`bw logout`

- Keresés és megjelenítés a Bitwarden páncéltermében:

`bw list items --search {{github}}`

- Egy adott elem megjelenítése a Bitwarden páncélteremből:

`bw get item {{github}}`

- Mappa létrehozása a Bitwarden trezorban:

`{{echo -n '{"name":"My Folder1"}' | base64}} | bw create folder`
