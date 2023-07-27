# ajson

> Voert JSONPath uit op JSON-objecten.
> Meer informatie: <https://github.com/spyzhov/ajson>.

- Lees JSON uit een bestand en voer een opgegeven JSONPath-expressie uit:

`ajson '{{$..json[?(@.path)]}}' {{pad/naar/bestand.json}}`

- Lees JSON van `stdin` en voer een gespecificeerde JSONPath-expressie uit:

`cat {{pad/naar/bestand.json}} | ajson '{{$..json[?(@.path)]}}'`

- Lees JSON van een URL en evalueer een opgegeven JSONPath-expressie:

`ajson '{{avg($..price)}}' '{{https://voorbeeld.com/api/}}'`

- Lees wat eenvoudige JSON en bereken een waarde:

`echo '{{3}}' | ajson '{{2 * pi * $}}'`
