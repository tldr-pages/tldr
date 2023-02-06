# shasum

> Kriptográfiai SHA ellenőrző összegek kiszámítása vagy ellenőrzése. További információ: <https://manned.org/shasum>.

- Számítsa ki egy fájl SHA1 ellenőrző összegét:

`shasum {{path/to/file}}`

- SHA256 ellenőrzőösszeg kiszámítása egy fájlhoz:

`shasum --algorithm 256 {{path/to/file}}`

- Több fájl SHA512 ellenőrző összegének kiszámítása:

`shasum --algorithm 512 {{path/to/file1}} {{path/to/file2}}`

- Az SHA256 ellenőrző összegek listájának kiszámítása és mentése egy fájlba:

`shasum --algorithm 256 {{path/to/file1}} {{path/to/file2}} > {{path/to/file.sha256}}`

- Egy fájl ellenőrzése az összegek listájával a könyvtár fájljaival:

`shasum --check {{path/to/file}}`

- Ellenőrizze az összegek listáját, és csak azoknál a fájloknál jelenítsen meg üzenetet, amelyeknél az ellenőrzés sikertelen:

`shasum --check --quiet {{path/to/file}}`

- Az SHA1 ellenőrző összeg kiszámítása a `stdin` címen:

`{{some_command}} | shasum`
