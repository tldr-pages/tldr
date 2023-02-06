# createrepo

> Inicializál egy RPM-tárat a megadott könyvtárban, beleértve az összes XML és SQLite fájlt. További információ: <https://manned.org/createrepo>.

- Egy alap tároló inicializálása egy könyvtárban:

`createrepo {{path/to/directory}}`

- Adattár inicializálása, a teszt RPM-ek kizárása és a verbózus naplók megjelenítése:

`createrepo -v -x {{test_*.rpm}} {{path/to/directory}}`

- Adattár inicializálása, SHA1 ellenőrző összeg algoritmus használatával és a szimbolikus hivatkozások figyelmen kívül hagyásával:

`createrepo -S -s {{sha1}} {{path/to/directory}}`
