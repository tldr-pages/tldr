# httpie

> Un instrument HTTP de linie de comandă prietenos cu utilizatorul.

- Trimiteți o solicitare de obținere (metoda implicită fără date de solicitare):

`http {{https://example.com}}`

- Trimiteți o solicitare POST (metoda implicită cu date de solicitare):

`http {{https://example.com}} {{hello=World}}`

- Trimiteți o solicitare POST cu intrare redirecționată:

`http {{https://example.com}} < {{file.json}}`

- Trimite o cerere PUT cu un anumit corp json:

`http PUT {{https://example.com/todos/7}} {{hello=world}}`

- Trimiteți o solicitare DELETE cu un antet de solicitare dat:

`http DELETE {{https://example.com/todos/7}} {{API-Key:foo}}`

- Afișați întregul schimb HTTP (atât cerere, cât și răspuns):

`http -v {{https://example.com}}`

- Descărcați un fișier:

`http --download {{https://example.com}}`
