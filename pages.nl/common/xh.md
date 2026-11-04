# xh

> Vriendelijke en snelle tool voor het versturen van HTTP-verzoeken.
> Opmerking: `xh`, geschreven in Rust, dient als een effectieve drop-in vervanging voor `http`.
> Zie ook: `http`, `curl`.
> Meer informatie: <https://github.com/ducaale/xh#usage>.

- Verstuur een GET-verzoek (toont response headers en inhoud):

`xh {{https://postman-echo.com/get}}`

- Verstuur een POST-verzoek met een JSON-body (sleutel-waardeparen worden toegevoegd aan een JSON-object op het hoogste niveau - bijv. `{"name": "john", "age": 25}`):

`xh post {{https://postman-echo.com/post}} {{name=john}} {{age=25}}`

- Verstuur een GET-verzoek met queryparameters (bijv. <https://postman-echo.com/response-headers?foo1=bar1&foo2=bar2>):

`xh get {{https://postman-echo.com/response-headers}} {{foo1==bar1}} {{foo2==bar2}}`

- Verstuur een GET-verzoek met een aangepaste header:

`xh get {{https://postman-echo.com}} {{header-name:header-value}}`

- Doe een GET-verzoek en sla de responsbody op in een bestand:

`xh {{[-d|--download]}} {{https://example.com}} {{[-o|--output]}} {{pad/naar/bestand}}`

- Simuleer het versturen van een verzoek zonder het daadwerkelijk te versturen:

`xh --offline {{get|delete|...}} {{https://example.com}}`

- Toon het equivalente `curl`-commando (dit verstuurt geen enkel verzoek):

`xh --{{curl|curl-long}} {{--follow --verbose get https://example.com user-agent:curl}}`
