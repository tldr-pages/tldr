# ajson

> Executes JSONPath with JSON document.
> More information: <https://github.com/spyzhov/ajson>.

- Read JSON from a file and execute JSONPath:

`ajson "$..json[?(@.path)]" example.json`

- Read JSON from STDIN and execute JSONPath:

`cat example.json | ajson "$..json[?(@.path)]"`

- Read JSON from `GET` request and calculate value:

`ajson "avg($..price)" "https://example.com/api/"`

- Curl JSON from `POST` request and calculate value:

`curl -s -d "param=value" -X POST http://example.com/ | ajson "sum($..price)"`

- Read simple JSON and calculate value:

`echo "3" | ajson "2 * pi * $"`
