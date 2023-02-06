# tmpmail

> Egy ideiglenes e-mail közvetlenül a terminálról, POSIX sh nyelven írva. További információ: <https://github.com/sdushantha/tmpmail>.

- Ideiglenes postafiók létrehozása:

`tmpmail --generate`

- Az üzenetek és numerikus azonosítójuk listázása:

`tmpmail`

- A legutóbb beérkezett e-mail megjelenítése:

`tmpmail --recent`

- Egy adott üzenet megnyitása:

`tmpmail {{email_id}}`

- E-mail megtekintése nyers szövegként, HTML-címkék nélkül:

`tmpmail --text`

- E-mail megnyitása egy adott böngészővel (alapértelmezett a w3m):

`tmpmail --browser {{browser}}`
