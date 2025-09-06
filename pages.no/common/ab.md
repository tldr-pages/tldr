# ab

> Apache HTTP server referansemåling verktøy.
> Mer informasjon: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Utfør 100 HTTP GET-forespørsler til en gitt URL:

`ab -n 100 {{url}}`

- Utfør 100 HTTP GET-forespørsler, i samtidige grupper på 10, til en URL:

`ab -n 100 -c 10 {{url}}`

- Utfør 100 HTTP POST-forespørsler til en URL, med å bruke en JSON-nyttelast fra en fil:

`ab -n 100 -T {{application/json}} -p {{vei/til/fil.json}} {{url}}`

- Bruk HTTP [K]eep Alive, dvs. utfør flere forespørsler i én HTTP-økt:

`ab -k {{url}}`

- Angi maksimalt antall sekunder å bruke på referansemåling:

`ab -t {{60}} {{url}}`
