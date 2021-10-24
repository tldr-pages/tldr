# ab

> Apache HTTP server Benchmarking Tool.
> Weitere Informationen: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Sende 100 HTTP GET Anfragen an eine URL:

`ab -n {{100}} {{url}}`

- Sende 100 HTTP GET Anfragen an eine URL, wovon bis zu 10 gleichzeitig bearbeitet werden:

`ab -n {{100}} -c {{10}} {{url}}`

- Wach halten:

`ab -k {{url}}`

- Lege die maximale Anzahl an Sekunden fest, die das Benchmarking dauern darf:

`ab -t {{60}} {{url}}`

- Sende 100 HTTP POST Anfragen an eine URL, wobei eine JSON Belastung aus einer Datei verwendet wird:

`ab -n {{100}} -T {{application/json}} -p {{pfad/zu/datei.json}} {{url}}`
