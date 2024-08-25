# httpie

> Een gebruiksvriendelijke HTTP-tool.
> Meer informatie: <https://github.com/httpie/httpie>.

- Verstuur een GET-verzoek (standaardmethode zonder verzoekgegevens):

`http {{https://example.com}}`

- Verstuur een POST-verzoek (standaardmethode met verzoekgegevens):

`http {{https://example.com}} {{hello=World}}`

- Verstuur een POST-verzoek met omgeleide invoer:

`http {{https://example.com}} < {{bestand.json}}`

- Verstuur een PUT-verzoek met een opgegeven JSON-body:

`http PUT {{https://example.com/todos/7}} {{hello=world}}`

- Verstuur een DELETE-verzoek met een opgegeven verzoekheader:

`http DELETE {{https://example.com/todos/7}} {{API-Key:foo}}`

- Toon de hele HTTP-uitwisseling (zowel verzoek als antwoord):

`http -v {{https://example.com}}`

- Download een bestand:

`http --download {{https://example.com}}`

- Volg redirects en toon tussenliggende verzoeken en antwoorden:

`http --follow --all {{https://example.com}}`
