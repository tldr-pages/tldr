# ajson

> Executes JSONPath on JSON objects.
> More information: <https://github.com/spyzhov/ajson>.

- Read JSON from a file and execute a specified JSONPath expression:

`ajson '{{$..json[?(@.path)]}}' {{path/to/file.json}}`

- Read JSON from stdin and execute a specified JSONPath expression:

`cat {{path/to/file.json}} | ajson '{{$..json[?(@.path)]}}'`

- Read JSON from a URL and evaluate a specified JSONPath expression:

`ajson '{{avg($..price)}}' '{{https://example.com/api/}}'`

- Read some simple JSON and calculate a value:

`echo '{{3}}' | ajson '{{2 * pi * $}}'`
