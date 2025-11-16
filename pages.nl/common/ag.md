# ag

> The Silver Searcher. Zoals `ack`, maar wil sneller zijn.
> Meer informatie: <https://manned.org/ag>.

- Zoek bestanden die `string` bevatten en druk de regelovereenkomsten in context af:

`ag string`

- Vind bestanden die `string` bevatten in een specifieke map:

`ag string {{pad/naar/map}}`

- Vind bestanden die `string` bevatten, maar vermeld alleen de bestandsnamen:

`ag {{[-l|--files-with-matches]}} string`

- Vind bestanden die `STRING` niet hoofdlettergevoelig bevatten en druk alleen de overeenkomst af in plaats van de hele regel:

`ag {{[-i|--ignore-case]}} {{[-o|--only-matching]}} STRING`

- Zoek `string` in bestanden met een naam die overeenkomt met `file_name`:

`ag string {{[-G|--file-search-regex]}} file_name`

- Vind bestanden waarvan de inhoud overeenkomt met een `regex`:

`ag '{{^ka(t|r)$}}'`

- Zoek bestanden met een naam die overeenkomt met `string`:

`ag {{[-g|--filename-pattern]}} string`
