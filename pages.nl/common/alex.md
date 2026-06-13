# alex

> Een tool die ongevoelig, onattent schrijven opvangt.
> Het helpt je bij het vinden van genderbegunstigende, polariserende, rasgerelateerde, onachtzame religie of andere ongelijke bewoordingen in de tekst.
> Meer informatie: <https://github.com/get-alex/alex>.

- Analyseer tekst van `stdin`:

`echo {{Zijn netwerk ziet er goed uit}} | alex --stdin`

- Analyseer alle bestanden in de huidige map:

`alex`

- Analyseer een specifiek bestand:

`alex {{tekstbestand.md}}`

- Analyseer alle Markdown-bestanden behalve `voorbeeld.md`:

`alex *.md !{{voorbeeld.md}}`
