# md5sum

> MD5 kriptográfiai ellenőrző összegek kiszámítása. További információ: <https://www.gnu.org/software/coreutils/md5sum>.

- Egy fájl MD5 ellenőrzőösszegének kiszámítása:

`md5sum {{path/to/file}}`

- Több fájl MD5 ellenőrzőösszegének kiszámítása:

`md5sum {{path/to/file1}} {{path/to/filen2}}`

- MD5 ellenőrző összeg kiszámítása a standard bemenetről:

`echo "{{text}}" | md5sum`

- MD5SUM-okból álló fájl beolvasása és annak ellenőrzése, hogy minden fájl ellenőrző összege megegyezik-e:

`md5sum --check {{path/to/file.md5}}`

- Csak a hiányzó fájlok vagy az ellenőrzés sikertelensége esetén jelenít meg üzenetet:

`md5sum --check --quiet {{path/to/file.md5}}`

- Csak olyan fájlokra vonatkozó üzenet megjelenítése, amelyeknél az ellenőrzés sikertelen, a hiányzó fájlok figyelmen kívül hagyása:

`md5sum --ignore-missing --check --quiet {{path/to/file.md5}}`
