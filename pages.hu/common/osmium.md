# osmium

> Többcélú eszköz az OpenStreetMap (OSM) fájlok kezelésére. További információ: <https://osmcode.org/osmium-tool/manual>.

- Fájlinformációk megjelenítése:

`osmium fileinfo {{path/to/input.osm}}`

- Tartalom megjelenítése:

`osmium show {{path/to/input.osm}}`

- Fájlformátum átalakítása PBF-ből XML-be:

`osmium cat {{path/to/input.osm.pbf}} -o {{path/to/output.osm}}`

- Földrajzi régió kivonása a megadott \[b\]ounding box alapján:

`osmium extract -b {{min_longitude}},{{min_latitude}},{{max_longitude}},{{max_latitude}} {{path/to/input.pbf}} -o {{path/to/output.pbf}}`

- Földrajzi régió kivonása GeoJSON fájl alapján:

`osmium extract -p {{path/to/polygon.geojson}} {{path/to/input.pbf}} -o {{path/to/output.pbf}}`

- Az összes "étterem" címkével ellátott objektum szűrése:

`osmium tags-filter {{path/to/input.pbf}} amenity=restaurant -o {{path/to/output.pbf}}`

- Szűrés az "út" objektumokra, amelyek "autópálya" címkével vannak ellátva:

`osmium tags-filter {{path/to/input.pbf}} w/highway -o {{path/to/output.pbf}}`

- "Út" és "kapcsolat" objektumok szűrése "épület" címkével:

`osmium tags-filter {{path/to/input.pbf}} wr/building -o {{path/to/output.pbf}}`
