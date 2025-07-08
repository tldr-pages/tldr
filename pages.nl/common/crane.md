# crane

> Hulpmiddel voor het beheren van containerimages.
> Sommige subcommando's zoals `pull`, `push`, `copy`, enz. hebben hun eigen gebruiksdocumentatie.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>.

- Voer een `crane` subcommando uit:

`crane {{subcommando}}`

- Sta het pushen van niet-distribueerbare (buitenlandse) lagen toe:

`crane --allow-nondistributable-artifacts {{subcommando}}`

- Sta het ophalen van afbeeldingsreferenties zonder TLS toe:

`crane --insecure {{subcommando}}`

- Geef het platform op in de vorm os/arch{{/variant}}{{:osversion}} (bijv. linux/amd64). (standaard alle):

`crane --platform {{platform}} {{subcommando}}`

- Schakel debuglogs in voor een subcommando:

`crane {{[-v|--verbose]}} {{subcommando}}`

- Toon de help voor een subcommando:

`crane {{[-h|--help]}} {{subcommando}}`
