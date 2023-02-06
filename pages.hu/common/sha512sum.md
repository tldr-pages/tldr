# sha512sum

> SHA512 kriptográfiai ellenőrző összegek kiszámítása. További információ: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Számítsa ki egy fájl SHA512 ellenőrző összegét:

`sha512sum {{path/to/file}}`

- Több fájl SHA512 ellenőrző összegének kiszámítása:

`sha512sum {{path/to/file1}} {{path/to/file2}}`

- Az SHA512 ellenőrző összegek listájának kiszámítása és mentése egy fájlba:

`sha512sum {{path/to/file1}} {{path/to/file2}} > {{path/to/file.sha512}}`

- SHA512 összegeket tartalmazó fájl beolvasása és annak ellenőrzése, hogy az összes fájl ellenőrző összege megegyezik-e:

`sha512sum --check {{path/to/file.sha512}}`

- Csak a hiányzó fájlok vagy az ellenőrzés sikertelensége esetén jeleníthet meg üzenetet:

`sha512sum --check --quiet {{path/to/file.sha512}}`

- Csak olyan fájlok esetén jeleníthet meg üzenetet, amelyek ellenőrzése sikertelen, a hiányzó fájlokat figyelmen kívül hagyja:

`sha512sum --ignore-missing --check --quiet {{path/to/file.sha512}}`
