# kiterunner scan

> A contextual web scanner for concurrently scanning API paths and web endpoints using kitebuilder wordlists.
> The `scan` subcommand targets one or multiple hosts with structured API requests.
> More information: <https://github.com/assetnote/kiterunner>.

- Scan a target with an Assetnote wordlist (e.g., first 5000 API routes):

`kiterunner scan {{https://target.com}} {{[-A|--assetnote-wordlist]}}={{apiroutes-210228:5000}}`

- Scan a target with a kitebuilder wordlist:

`kiterunner scan {{https://target.com}} {{[-w|--kitebuilder-list]}} {{wordlist.kite}}`

- Scan multiple hosts from a file with a kitebuilder wordlist:

`kiterunner scan {{hosts.txt}} {{[-w|--kitebuilder-list]}} {{wordlist.kite}}`

- Scan with an Assetnote wordlist and JSON output:

`kiterunner scan {{https://target.com}} {{[-A|--assetnote-wordlist]}}={{apiroutes-210228:5000}} -o {{json}}`

- Scan with custom concurrency settings for performance:

`kiterunner scan {{https://target.com}} {{[-w|--kitebuilder-list]}} {{wordlist.kite}} {{[-x|--max-connection-per-host]}} {{5}} {{[-j|--max-parallel-hosts]}} {{100}}`

- Scan with a wordlist as a normal wordlist, disabling depth scanning:

`kiterunner scan {{https://target.com}} {{[-w|--kitebuilder-list]}} {{rafter.txt}} {{[-d|--preflight-depth]}} {{0}}`

- Scan with custom headers and ignore specific content length responses:

`kiterunner scan {{https://target.com}} {{[-w|--kitebuilder-list]}} {{wordlist.kite}} {{[-H|--header]}} "{{Authorization: Bearer token}}" --ignore-length={{100-105}}`

- Perform a full kitebuilder scan without phase scanning:

`kiterunner scan {{https://target.com}} {{[-w|--kitebuilder-list]}} {{wordlist.kite}} --kitebuilder-full-scan`
