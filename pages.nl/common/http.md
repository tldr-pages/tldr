# http

> HTTPie: HTTP client, bedoeld om gebruiksvriendelijker te zijn dan cURL.
> Meer informatie: <https://httpie.org>.

- Download een URL naar een bestand:

`http --download {{example.org}}`

- Verstuur formulier-gecodeerde data:

`http --form {{example.org}} {{naam='bob'}} {{profielfoto@'bob.png'}}`

- Verstuur een JSON-object:

`http {{example.org}} {{naam='bob'}}`

- Specificeer een HTTP-methode:

`http {{HEAD}} {{example.org}}`

- Voeg een extra header toe:

`http {{example.org}} {{X-MyHeader:123}}`

- Geef een gebruikersnaam en wachtwoord op voor serverauthenticatie:

`http --auth {{gebruikersnaam:wachtwoord}} {{example.org}}`

- Specificeer de onbewerkte request body via `stdin`:

`cat {{data.txt}} | http PUT {{example.org}}`
