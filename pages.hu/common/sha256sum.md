# sha256sum

> SHA256 kriptográfiai ellenőrző összegek kiszámítása. További információ: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Számítsa ki egy fájl SHA256 ellenőrző összegét:

`sha256sum {{path/to/file}}`

- Több fájl SHA256 ellenőrző összegének kiszámítása:

`sha256sum {{path/to/file1}} {{path/to/file2}}`

- Az SHA256 ellenőrző összegek listájának kiszámítása és mentése egy fájlba:

`sha256sum {{path/to/file1}} {{path/to/file2}} > {{path/to/file.sha256}}`

- SHA256 összegeket tartalmazó fájl beolvasása és annak ellenőrzése, hogy az összes fájl ellenőrző összege megegyezik-e:

`sha256sum --check {{path/to/file.sha256}}`

- Csak a hiányzó fájlok vagy az ellenőrzés sikertelensége esetén jeleníthet meg üzenetet:

`sha256sum --check --quiet {{path/to/file.sha256}}`

- Csak olyan fájlok esetén jeleníthet meg üzenetet, amelyek ellenőrzése sikertelen, a hiányzó fájlokat figyelmen kívül hagyja:

`sha256sum --ignore-missing --check --quiet {{path/to/file.sha256}}`
