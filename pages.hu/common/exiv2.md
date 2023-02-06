# exiv2

> Képi metaadat-manipuláló eszköz. További információ: <https://www.exiv2.org/manpage.html>.

- A kép Exif metaadatainak összefoglalójának kinyomtatása:

`exiv2 {{path/to/file}}`

- Az összes metaadat (Exif, IPTC, XMP) nyomtatása értelmezett értékekkel:

`exiv2 -P kt {{path/to/file}}`

- Minden metaadat nyomtatása nyers értékekkel:

`exiv2 -P kv {{path/to/file}}`

- Minden metaadat törlése a képről:

`exiv2 -d a {{path/to/file}}`

- Az összes metaadat törlése a fájl időbélyegének megőrzésével:

`exiv2 -d a -k {{path/to/file}}`

- A fájl átnevezése, a metaadatokból származó dátum és időpont előtaggal (nem a fájl időbélyegéből):

`exiv2 -r {{'%Y%m%d_%H%M%S_:basename:'}} {{path/to/file}}`
