# httpie

> Egy felhasználóbarát parancssori HTTP eszköz. További információ: <https://github.com/httpie/httpie>.

- GET-kérelem küldése (alapértelmezett módszer kérési adatok nélkül):

`http {{https://example.com}}`

- POST-kérelem küldése (alapértelmezett módszer kérési adatokkal):

`http {{https://example.com}} {{hello=World}}`

- POST-kérelem küldése átirányított bemenettel:

`http {{https://example.com}} < {{file.json}}`

- PUT kérés küldése adott JSON testtel:

`http PUT {{https://example.com/todos/7}} {{hello=world}}`

- DELETE-kérelem küldése adott kérési fejléccel:

`http DELETE {{https://example.com/todos/7}} {{API-Key:foo}}`

- A teljes HTTP üzenetváltás megjelenítése (kérés és válasz):

`http -v {{https://example.com}}`

- Fájl letöltése:

`http --download {{https://example.com}}`

- Kövesse az átirányításokat, és mutassa meg a köztes kéréseket és válaszokat:

`http --follow --all {{https://example.com}}`
