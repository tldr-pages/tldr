# sha224sum

> SHA224 kriptográfiai ellenőrző összegek kiszámítása. További információ: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Számítsa ki egy fájl SHA224 ellenőrző összegét:

`sha224sum {{path/to/file}}`

- Több fájl SHA224 ellenőrzőösszegének kiszámítása:

`sha224sum {{path/to/file1}} {{path/to/file2}}`

- Az SHA224 ellenőrző összegek listájának kiszámítása és mentése egy fájlba:

`sha224sum {{path/to/file1}} {{path/to/file2}} > {{path/to/file.sha224}}`

- SHA224 összegeket tartalmazó fájl beolvasása és annak ellenőrzése, hogy az összes fájl ellenőrző összege megegyezik-e:

`sha224sum --check {{path/to/file.sha224}}`

- Csak a hiányzó fájlok vagy az ellenőrzés sikertelensége esetén jeleníthet meg üzenetet:

`sha224sum --check --quiet {{path/to/file.sha224}}`

- Csak olyan fájlok esetén jeleníthet meg üzenetet, amelyek ellenőrzése sikertelen, a hiányzó fájlokat figyelmen kívül hagyja:

`sha224sum --ignore-missing --check --quiet {{path/to/file.sha224}}`
