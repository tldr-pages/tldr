# file

> A fájltípus meghatározása. További információ: <https://manned.org/file>.

- A megadott fájl típusának leírása. Jól működik a fájlkiterjesztés nélküli fájlok esetében:

`file {{path/to/file}}`

- Nézzen bele egy zippelt fájlba, és határozza meg a benne lévő fájltípus(oka)t:

`file -z {{foo.zip}}`

- Engedélyezze a fájl működését speciális vagy eszközfájlokkal:

`file -s {{path/to/file}}`

- Ne álljon meg az első fájltípus egyezésnél; folytassa a keresést a fájl végéig:

`file -k {{path/to/file}}`

- Határozza meg a fájl MIME kódolási típusát:

`file -i {{path/to/file}}`
