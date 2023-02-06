# tomb

> Titkosított tárolási könyvtárak kezelése, amelyeket biztonságosan lehet szállítani és elrejteni egy fájlrendszerben. További információ: <https://www.dyne.org/software/tomb/>.

- Hozzon létre egy új sírhelyet, amelynek kezdeti mérete 100 MB:

`tomb dig -s {{100}} {{encrypted_directory.tomb}}`

- Új kulcsfájl létrehozása, amely egy sírhely lezárására használható; a felhasználónak jelszót kell megadnia a kulcshoz:

`tomb forge {{encrypted_directory.tomb.key}}`

- Kényszerített új kulcs létrehozása, még akkor is, ha a sírhely nem engedélyezi a kulcs hamisítását (a swap miatt):

`tomb forge {{encrypted_directory.tomb.key}} -f`

- Üres sírhely inicializálása és lezárása a `forge` segítségével készített kulccsal:

`tomb lock {{encrypted_directory.tomb}} -k {{encrypted_directory.tomb.key}}`

- A sírhely (alapértelmezés szerint a `/media`) kulcsának használatával történő mountolása, így az normál fájlrendszeri könyvtárként használhatóvá válik:

`tomb open {{encrypted_directory.tomb}} -k {{encrypted_directory.tomb.key}}`

- Sírhely bezárása (sikertelen, ha a sírhelyet egy folyamat használja):

`tomb close {{encrypted_directory.tomb}}`

- Az összes nyitott sírhely erőszakos bezárása, megölve az azokat használó alkalmazásokat:

`tomb slam all`

- Az összes nyitott sírhely listázása:

`tomb list`
