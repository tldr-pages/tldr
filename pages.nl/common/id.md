# id

> Toon de huidige gebruikers- en groepsidentiteit.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/id-invocation.html>.

- Toon de ID (UID), groep-ID (GID) en groepen waartoe de huidige gebruiker behoort:

`id`

- Toon de identiteit van de huidige gebruiker:

`id {{[-un|--user --name]}}`

- Toon de identiteit van de huidige gebruiker als een nummer:

`id {{[-u|--user]}}`

- Toon de identiteit van de huidige primaire groepsidentiteit:

`id {{[-gn|--group --name]}}`

- Toon de identiteit van de huidige primaire groepsidentiteit als een nummer:

`id {{[-g|--group]}}`

- Toon alle groupen waartoe de huidige gebruiker behoort:

`id {{[-Gn|--groups --name]}}`

- Toon de ID (UID), groep-ID (GID) en groepen waartoe een willekeurige gebruiker behoort:

`id {{gebruikersnaam}}`

- Sla het opzoeken van de naam over en specificeer het UID-nummer expliciet:

`id +{{uid_number}}`
