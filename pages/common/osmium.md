# osmium

> Multipurpose tool for handling OpenStreetMap (OSM) files.
> More information: <https://osmcode.org/osmium-tool/manual>.

- Show file information:

`osmium fileinfo {{path/to/input.osm}}`

- Display contents:

`osmium show {{path/to/input.osm}}`

- Convert file format from PBF into XML:

`osmium cat {{path/to/input.osm.pbf}} {{[-o|--output]}} {{path/to/output.osm}}`

- Extract a geographic region by the given [b]ounding box:

`osmium extract {{[-b|--bbox]}} {{min_longitude}},{{min_latitude}},{{max_longitude}},{{max_latitude}} {{path/to/input.pbf}} {{[-o|--output]}} {{path/to/output.pbf}}`

- Extract a geographic region by a GeoJSON file:

`osmium extract {{[-p|--polygon]}} {{path/to/polygon.geojson}} {{path/to/input.pbf}} {{[-o|--output]}} {{path/to/output.pbf}}`

- Filter all objects tagged as "restaurant":

`osmium tags-filter {{path/to/input.pbf}} amenity=restaurant {{[-o|--output]}} {{path/to/output.pbf}}`

- Filter for "way" objects tagged as "highway":

`osmium tags-filter {{path/to/input.pbf}} w/highway {{[-o|--output]}} {{path/to/output.pbf}}`

- Filter "way" and "relation" objects tagged as "building":

`osmium tags-filter {{path/to/input.pbf}} wr/building {{[-o|--output]}} {{path/to/output.pbf}}`
