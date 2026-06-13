# kiterunner wordlist

> A contextual web scanner for managing wordlists used in API and web endpoint discovery.
> The `wordlist` subcommand handles listing and saving wordlists in `~/.cache/kiterunner`.
> More information: <https://github.com/assetnote/kiterunner#usage>.

- List all cached and available Assetnote wordlists:

`kiterunner wordlist list`

- List wordlists with JSON output:

`kiterunner wordlist list {{[-o|--output]}} {{json}}`

- List wordlists with verbose debug output:

`kiterunner wordlist list {{[-v|--verbose]}} {{debug}}`

- Save a specific Assetnote wordlist by alias:

`kiterunner wordlist save {{apiroutes-210328}}`

- Save a specific Assetnote wordlist by full filename:

`kiterunner wordlist save {{path/to/httparchive_apiroutes_2024_05_28.txt}}`

- Save multiple wordlists by alias:

`kiterunner wordlist save {{apiroutes-210328,aspx-210328}}`

- Save a wordlist with quiet mode to suppress output:

`kiterunner wordlist save {{apiroutes-210328}} {{[-q|--quiet]}}`
