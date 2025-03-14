# gcrane

> Beheer tool voor containerafbeeldingen.
> Deze tool implementeert een superset van de `crane`-commando's, met aanvullende commando's die specifiek zijn voor `gcr.io`.
> Sommige subcommando's zoals `append`, `auth`, `copy`, enz. hebben hun eigen gebruiksdocumentatie die te vinden is onder `crane`.
> Sommige subcommando's zoals `completion`, `gc`, `help` zijn specifiek voor gcrane en hebben hun eigen gebruiksdocumentatie.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Voer een `gcrane`-subcommando uit:

`gcrane {{subcommand}}`

- Sta het pushen van niet-distributieve (vreemde) lagen toe:

`gcrane --allow-nondistributable-artifacts {{subcommand}}`

- Sta het ophalen van afbeeldingsreferenties zonder TLS toe:

`gcrane --insecure {{subcommand}}`

- Specificeer het platform in de vorm os/arch{{/variant}}{{:osversion}} (bijv. linux/amd64). (standaard alles):

`gcrane --platform {{platform}} {{subcommand}}`

- Schakel debuglogs in:

`gcrane {{[-v|--verbose]}} {{subcommand}}`

- Toon de help:

`gcrane {{[-h|--help]}}`
