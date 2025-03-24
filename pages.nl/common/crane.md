# crane

> Hulpmiddel voor het beheren van containerimages.
> Sommige subcommando's zoals `pull`, `push`, `copy`, enz. hebben hun eigen gebruiksdocumentatie.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>.

- Voer een `crane` subcommando uit:

`crane {{subcommand}}`

- Sta het pushen van niet-distribueerbare (buitenlandse) lagen toe:

`crane --allow-nondistributable-artifacts {{subcommand}}`

- Sta het ophalen van afbeeldingsreferenties zonder TLS toe:

`crane --insecure {{subcommand}}`

- Geef het platform op in de vorm os/arch{{/variant}}{{:osversion}} (bijv. linux/amd64). (standaard alle):

`crane --platform {{platform}} {{subcommand}}`

- Schakel debuglogs in voor een subcommando:

`crane {{[-v|--verbose]}} {{subcommand}}`

- Toon help voor een subcommando:

`crane {{[-h|--help]}} {{subcommand}}`
