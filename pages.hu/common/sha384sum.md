# sha384sum

> SHA384 kriptográfiai ellenőrző összegek kiszámítása. További információ: <https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html>.

- Számítsa ki egy fájl SHA384 ellenőrző összegét:

`sha384sum {{path/to/file}}`

- Több fájl SHA384 ellenőrzőösszegének kiszámítása:

`sha384sum {{path/to/file1}} {{path/to/file2}}`

- Az SHA384 ellenőrző összegek listájának kiszámítása és mentése egy fájlba:

`sha384sum {{path/to/file1}} {{path/to/file2}} > {{path/to/file.sha384}}`

- SHA384 összegeket tartalmazó fájl beolvasása és annak ellenőrzése, hogy az összes fájl ellenőrző összege megegyezik-e:

`sha384sum --check {{path/to/file.sha384}}`

- Csak a hiányzó fájlok vagy az ellenőrzés sikertelensége esetén jeleníthet meg üzenetet:

`sha384sum --check --quiet {{path/to/file.sha384}}`

- Csak olyan fájlok esetén jeleníthet meg üzenetet, amelyek ellenőrzése sikertelen, a hiányzó fájlokat figyelmen kívül hagyja:

`sha384sum --ignore-missing --check --quiet {{path/to/file.sha384}}`
