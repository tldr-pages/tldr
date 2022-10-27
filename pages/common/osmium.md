# osmium

> Multipurpose tool for handling OpenStreetMap (OSM) files.
> More information: <https://osmcode.org/osmium-tool/manual>.

- Show file information:

`osmium fileinfo {{path/to/input.osm}}`

- Display contents:

`osmium show {{path/to/input.osm}}`

- Convert file format from PBF into XML:

`osmium cat {{path/to/input.osm.pbf}} -o {{path/to/output.osm}}`

- Extract a geographic region by the given [b]ounding box:

`osmium extract -b {{min_longitude}},{{min_latitude}},{{max_longitude}},{{max_latitude}} {{path/to/input.pbf}} -o {{path/to/output.pbf}}`

- Extract a geographic region by a GeoJSON file:

`osmium extract -p {{path/to/polygon.geojson}} {{path/to/input.pbf}} -o {{path/to/output.pbf}}`

- Filter all objects tagged as "restaurant":

`osmium tags-filter {{path/to/input.pbf}} amenity=restaurant -o {{path/to/output.pbf}}`

- Filter for "way" objects tagged as "highway":

`osmium tags-filter {{path/to/input.pbf}} w/highway -o {{path/to/output.pbf}}`

- Filter "way" and "relation" objects tagged as "building":

`osmium tags-filter {{path/to/input.pbf}} wr/building -o {{path/to/output.pbf}}`
