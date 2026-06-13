# ab

> Apache HTTP-serverbenchmarktool.
> Meer informatie: <https://httpd.apache.org/docs/current/programs/ab.html>.

- Voer 100 HTTP GET-verzoeken uit naar een bepaalde URL:

`ab -n 100 {{url}}`

- Voer 100 HTTP GET-verzoeken uit, in gelijktijdige batches van 10, naar een URL:

`ab -n 100 -c 10 {{url}}`

- Voer 100 HTTP POST-verzoeken uit naar een URL, met behulp van een JSON-payload uit een bestand:

`ab -n 100 -T {{application/json}} -p {{pad/naar/bestand.json}} {{url}}`

- Gebruik HTTP Keep Alive, d.w.z. voer meerdere verzoeken uit binnen één HTTP-sessie:

`ab -k {{url}}`

- Stel het maximale aantal seconden in dat je wil besteden aan benchmarking:

`ab -t {{60}} {{url}}`

- Schrijf de resultaten naar een CSV bestand:

`ab -e {{pad/naar/bestand.csv}}`
