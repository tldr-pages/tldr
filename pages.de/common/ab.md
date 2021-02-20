# ab

> Apache Benchmarking Tool. Das einfachste Tool um eine Belastungsprobe durchzuführen.
> Weitere Information: <https://httpd.apache.org/docs/2.4/programs/ab.html>.

- Sende 100 HTTP GET Anfrage an eine gegebene URL:

`ab -n {{100}} {{url}}`

- Sende 10 HTTP GET Anfragen an eine gegebene URL, wovon bis zu 10 gleichzeitig bearbeitet werden:

`ab -n {{100}} -c {{10}} {{url}}`

- Wach halten:

`ab -k {{url}}`

- Setze die maximale Anzahl an Sekunden, die das Benchmarking dauern darf:

`ab -t {{60}} {{url}}`

- Sende 100 HTTP POST Anfragen an eine gegebene URL, wobei eine JSON Belastung aus einer Datei verwendet wird:

`ab -n {{100}} -T {{application/json}} -p {{daten.json}} {{url}}`
