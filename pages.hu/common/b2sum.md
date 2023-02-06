# b2sum

> BLAKE2 kriptográfiai ellenőrző összegek kiszámítása. További információ: <https://www.gnu.org/software/coreutils/b2sum>.

- Egy fájl BLAKE2 ellenőrzőösszegének kiszámítása:

`b2sum {{path/to/file}}`

- BLAKE2 ellenőrző összegek kiszámítása több fájlhoz:

`b2sum {{path/to/file1}} {{path/to/file2}}`

- A BLAKE2 ellenőrző összeg kiszámítása a `stdin` oldalról:

`{{some_command}} | b2sum`

- Olvassa be a BLAKE2 összegeket és fájlneveket tartalmazó fájlt, és ellenőrizze, hogy az összes fájl ellenőrző összege megegyezik-e:

`b2sum --check {{path/to/file.b2}}`

- Csak a hiányzó fájlok vagy az ellenőrzés sikertelensége esetén jelenít meg üzenetet:

`b2sum --check --quiet {{path/to/file.b2}}`

- Csak olyan fájlok esetén jelenít meg üzenetet, amelyek ellenőrzése sikertelen, a hiányzó fájlokat figyelmen kívül hagyja:

`b2sum --ignore-missing --check --quiet {{path/to/file.b2}}`
