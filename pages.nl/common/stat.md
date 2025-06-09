# stat

> Toon bestands- en bestandssysteeminformatie.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html>.

- Toon eigenschappen van een specifiek bestand zoals grootte, permissies, aanmaak- en toegangsdatums en meer:

`stat {{pad/naar/bestand}}`

- Toon eigenschappen van een specifiek bestand zoals grootte, permissies, aanmaak- en toegangsdatums en meer zonder labels:

`stat {{[-t|--terse]}} {{pad/naar/bestand}}`

- Toon informatie over het bestandssysteem waar een specifiek bestand zich bevindt:

`stat {{[-f|--file-system]}} {{pad/naar/bestand}}`

- Toon alleen octale bestandspermissies:

`stat {{[-c|--format]}} "%a %n" {{pad/naar/bestand}}`

- Toon de eigenaar en groep van een specifiek bestand:

`stat {{[-c|--format]}} "%U %G" {{pad/naar/bestand}}`

- Toon de grootte van een specifiek bestand in bytes:

`stat {{[-c|--format]}} "%s %n" {{pad/naar/bestand}}`
