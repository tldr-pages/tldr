# kiterunner kb

> A contextual web scanner for manipulating kitebuilder schemas used in API and web endpoint discovery.
> The `kb` subcommand handles schema compilation, conversion, parsing, and request replay.
> More information: <https://github.com/assetnote/kiterunner>.

- Compile a kitebuilder schema from JSON to a kite file:

`kiterunner kb compile {{path/to/wordlist.json}} {{path/to/wordlist.kite}}`

- Convert a kite file to a text wordlist:

`kiterunner kb convert {{path/to/wordlist.kite}} {{path/to/wordlist.txt}}`

- Convert a text wordlist to a kite file:

`kiterunner kb convert {{path/to/wordlist.txt}} {{path/to/wordlist.kite}}`

- Convert a kite file to a JSON schema:

`kiterunner kb convert {{path/to/wordlist.kite}} {{path/to/wordlist.json}}`

- Parse a kitebuilder schema and output prettified JSON data:

`kiterunner kb parse {{path/to/wordlist.json}} {{[-o|--output]}} {{json}}`

- Parse a kite file and output prettified text data:

`kiterunner kb parse {{path/to/wordlist.kite}} {{[-o|--output]}} {{text}}`

- Replay a specific request from a kitebuilder schema output:

`kiterunner kb replay {{[-w|--kitebuilder-list]}} {{path/to/wordlist.kite}} "{{request_output}}"`

- Replay a request through a proxy for inspection:

`kiterunner kb replay {{[-w|--kitebuilder-list]}} {{path/to/wordlist.kite}} {{[-p|--proxy]}} {{http://localhost:8080}} "{{request_output}}"`
