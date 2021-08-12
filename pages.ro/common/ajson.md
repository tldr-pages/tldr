# ajson

> Execută JSonPath pe obiecte JSON.
> Mai multe informaţii: <https://github.com/spyzhov/ajson>

- Citiți JSON dintr-un fișier și executați o expresie JSonPath specificată:

`ajson '{{$..json[?(@.path)]}}' {{path/to/file.json}}`

- Citiți JSON din stdin și executați o expresie JSonPath specificată:

`cat {{path/to/file.json}} | ajson '{{$..json[?(@.path)]}}'`

- Citiți JSON dintr-un URL și evaluați o expresie JSonPath specificată:

`ajson '{{avg($..price)}}' '{{https://example.com/api/}}'`

- Citește unele JSON simplu și se calculează o valoare:

`echo '{{3}}' | ajson '{{2 * pi * $}}'`
