# kiterunner brute

> A contextual web scanner for bruteforcing API paths and web endpoints using wordlists.
> The `brute` subcommand targets one or multiple hosts.
> More information: <https://github.com/assetnote/kiterunner>.

- Bruteforce a target with an Assetnote wordlist (e.g., first 20,000 API routes):

`kiterunner brute {{https://example.com}} {{[-A|--assetnote-wordlist]}} {{apiroutes-210328:20000}}`

- Bruteforce a target with a custom wordlist:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}}`

- Bruteforce using a dirsearch-style wordlist with extension substitution:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{path/to/dirsearch.txt}} {{[-D|--dirsearch-compat]}} {{[-e|--extensions]}} {{json,txt}}`

- Bruteforce with specific file extensions appended and output in JSON format:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}} {{[-e|--extensions]}} {{aspx,ashx}} {{[-o|--output]}} {{json}}`

- Bruteforce a list of targets from a file with custom concurrency settings for performance:

`kiterunner brute {{path/to/targets.txt}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}} {{[-x|--max-connection-per-host]}} {{5}} {{[-j|--max-parallel-hosts]}} {{100}}`

- Bruteforce and ignore specific content length responses:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}} --ignore-length {{100-105}}`

- Bruteforce with custom HTTP headers:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}} {{[-H|--header]}} "{{Authorization: Bearer token}}"`

- Bruteforce a list of targets from a file with fail status code filtering:

`kiterunner brute {{path/to/targets.txt}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}} --fail-status-codes {{400,401,404}}`
