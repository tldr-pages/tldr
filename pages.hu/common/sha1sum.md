# sha1sum

> SHA1 kriptográfiai ellenőrző összegek kiszámítása. További információ: <https://www.gnu.org/software/coreutils/sha1sum>.

- Számítsa ki egy fájl SHA1 ellenőrző összegét:

`sha1sum {{path/to/file}}`

- Több fájl SHA1 ellenőrzőösszegének kiszámítása:

`sha1sum {{path/to/file1}} {{path/to/file2}}`

- Az SHA1 ellenőrző összegek listájának kiszámítása és mentése egy fájlba:

`sha1sum {{path/to/file1}} {{path/to/file2}} > {{path/to/file.sha1}}`

- SHA1 összegeket tartalmazó fájl beolvasása és annak ellenőrzése, hogy az összes fájl ellenőrző összege megegyezik-e:

`sha1sum --check {{path/to/file.sha1}}`

- Csak a hiányzó fájlok vagy az ellenőrzés sikertelensége esetén jeleníthet meg üzenetet:

`sha1sum --check --quiet {{path/to/file.sha1}}`

- Csak olyan fájlok esetén jeleníthet meg üzenetet, amelyek ellenőrzése sikertelen, a hiányzó fájlokat figyelmen kívül hagyja:

`sha1sum --ignore-missing --check --quiet {{path/to/file.sha1}}`
