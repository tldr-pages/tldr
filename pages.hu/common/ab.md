# ab

> Apache HTTP szerver benchmarking eszköz. További információ: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Végezzen el 100 HTTP GET-kérést egy adott URL-címre:

`ab -n {{100}} {{url}}`

- Végrehajt 100 HTTP GET-kérést egyidejűleg 10 darabos tételekben egy URL-címre:

`ab -n {{100}} -c {{10}} {{url}}`

- 100 HTTP POST-kérés végrehajtása egy URL-címre, egy fájlból származó JSON-feltöltés felhasználásával:

`ab -n {{100}} -T {{application/json}} -p {{path/to/file.json}} {{url}}`

- HTTP \[K\]eep Alive használata, azaz több kérés végrehajtása egy HTTP-munkameneten belül:

`ab -k {{url}}`

- Állítsa be a teljesítményértékelésre fordítandó maximális másodpercek számát:

`ab -t {{60}} {{url}}`
