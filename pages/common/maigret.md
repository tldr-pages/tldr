# maigret

> Collect OSINT information about usernames across thousands of websites.
> Note: The Maigret database is a local JSON file bundled with the tool.
> See also: `sherlock`.
> More information: <https://maigret.readthedocs.io/en/latest/usage-examples.html>.

- Search for accounts using one or more usernames from the Maigret database:

`maigret {{username1 username2 ...}}`

- Search for accounts and generate reports in various formats:

`maigret {{username}} {{--txt|--csv|--html|--xmind|--pdf|--graph|--json simple|--json ndjson}}`

- Proxy search requests through a proxy:

`maigret {{username}} {{[-p|--proxy]}} {{socks5://127.0.0.1:9050|http://127.0.0.1:8080}}`

- Launch Maigret Web Interface (default port `5000`):

`maigret --web {{5000}}`

- Limit search to a certain number of top-ranked sites from the Maigret database:

`maigret {{username}} --top-sites {{500}}`

- Search all available sites in the Maigret database:

`maigret {{username}} {{[-a|--all-sites]}}`

- Search for accounts on specific sites only (useful for targeted or faster searches):

`maigret {{username}} --site {{twitter}} --site {{github}}`
