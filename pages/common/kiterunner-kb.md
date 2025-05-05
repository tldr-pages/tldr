# kiterunner kb

> A contextual web scanner for manipulating kitebuilder schemas used in API and web endpoint discovery.
> The `kb` subcommand handles schema compilation, conversion, parsing, and request replay.
> More information: <https://github.com/assetnote/kiterunner>.

- Compile a kitebuilder schema from JSON to a kite file:

`kiterunner kb compile {{wordlist.json}} {{wordlist.kite}}`

- Convert a kite file to a text wordlist:

`kiterunner kb convert {{wordlist.kite}} {{wordlist.txt}}`

- Convert a text wordlist to a kite file:

`kiterunner kb convert {{wordlist.txt}} {{wordlist.kite}}`

- Convert a kite file to a JSON schema:

`kiterunner kb convert {{wordlist.kite}} {{wordlist.json}}`

- Parse a kitebuilder schema and output prettified JSON data:

`kiterunner kb parse {{wordlist.json}} {{[-o|--output]}} {{json}}`

- Parse a kite file and output prettified text data:

`kiterunner kb parse {{wordlist.kite}} {{[-o|--output]}} {{text}}`

- Replay a specific request from a kitebuilder schema output:

`kiterunner kb replay {{[-w|--kitebuilder-list]}} {{wordlist.kite}} "{{request_output}}"`

- Replay a request through a proxy for inspection:

`kiterunner kb replay {{[-w|--kitebuilder-list]}} {{wordlist.kite}} {{[-p|--proxy]}} {{http://localhost:8080}} "{{request_output}}"`
