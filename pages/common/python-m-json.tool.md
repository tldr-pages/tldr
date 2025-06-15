# python -m json.tool

> Validate and pretty-print JSON data.
> Part of Python's standard library.
> More information: <https://docs.python.org/library/json.html#module-json.tool>.

- Pretty-print JSON from a file:

`python -m json.tool {{path/to/file.json}}`

- Validate and pretty-print JSON from standard input:

`echo '{{{"key": "value"}}}' | python -m json.tool`
