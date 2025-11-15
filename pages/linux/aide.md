# aide

> Advanced Intrusion Detection Environment to validate file integrity.
> More information: <https://manned.org/aide>.

- Initialize the database:

`sudo aide {{[-i|--init]}}`

- Check the database for inconsistencies:

`sudo aide {{[-C|--check]}}`

- Compare two databases according to definitions in the config file:

`sudo aide {{[-E|--compare]}}`

- Check and update the database non-interactively:

`sudo aide {{[-u|--update]}}`

- Define a config file to override the default `./aide.conf`:

`sudo aide {{[-c|--config]}} {{path/to/config_file}}`

- Use `regex` to limit AIDE to a specific string:

`sudo aide {{[-l|--limit]}} {{regex}}`

- Send reporter results to a URL:

`sudo aide {{[-r|--report]}} {{reporterurl}}`
