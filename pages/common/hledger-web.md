# hledger-web

> A robust, friendly plain text accounting app (the web UI & API).
> More information: <https://hledger.org>.

- Start the web app, and a browser if possible, for local viewing and adding:

`hledger-web`

- As above but with a specified file, and allowing editing of existing data:

`hledger-web --file {{path/to/file.journal}} --allow edit`

- Start the web app only, allowing incoming connections to this host & port:

`hledger-web --serve --host {{my.host.name}} --port 8000`

- Start the web app's JSON API only, allowing read access only:

`hledger-web --serve-api --host {{my.host.name}} --allow view`

- Show amounts converted to current market value, when possible:

`hledger-web --value now --infer-market-prices`

- Show command-line help:

`hledger-web --help`

- Show the manual in Info format if possible:

`hledger-web --info`
