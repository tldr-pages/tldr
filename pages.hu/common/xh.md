# xh

> Barátságos és gyors eszköz HTTP-kérések küldésére. További információ: <https://github.com/ducaale/xh>.

- GET-kérés küldése:

`xh {{httpbin.org/get}}`

- POST-kérelem küldése JSON-testtel (a kulcs-érték párokat egy felső szintű JSON-objektumhoz adjuk hozzá - pl. `{"name": "john", "age": 25}`):

`xh post {{httpbin.org/post}} {{name=john}} {{age:=25}}`

- GET-kérés küldése lekérdezési paraméterekkel (pl. `first_param=5&second_param=true`):

`xh get {{httpbin.org/get}} {{first_param==5}} {{second_param==true}}`

- GET-kérelem küldése egyéni fejléccel:

`xh get {{httpbin.org/get}} {{header-name:header-value}}`

- GET-kérés küldése és a választest mentése egy fájlba:

`xh --download {{httpbin.org/json}} --output {{path/to/file}}`
