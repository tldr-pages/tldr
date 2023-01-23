# unar

> Tartalom kivonása archívumfájlokból. További információ: <https://manned.org/unar>.

- Egy archívum kivonatolása az aktuális könyvtárba:

`unar {{archive}}`

- Egy archívum kibontása a megadott könyvtárba:

`unar -o {{path/to/directory}} {{archive}}`

- Kényszeríti a felülírást, ha a kicsomagolandó fájlok már léteznek:

`unar -f {{archive}}`

- Átnevezés kényszerítése, ha a kicsomagolandó fájlok már léteznek:

`unar -r {{archive}}`

- Kihagyás kényszerítése, ha a kicsomagolandó fájlok már léteznek:

`unar -s {{archive}}`
