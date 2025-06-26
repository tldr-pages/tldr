# aide

> Advanced Intrusion Detection Environment to validate file integrity.
> More information: <https://manned.org/aide>.

- Initialize the database:

`aide {{[-i|--init]}}`

- Check the database for inconsistencies:

`aide {{[-C|--check]}}`

- Compare two databases according to definitions in the config file:

`aide {{[-E|--compare]}}`

- Check and update the database non-interactively:

`aide {{[-u|--update]}}`

- Define a config file to override the default {{./aide.conf}}:

`aide {{[-c|--config=]}} {{path/to/configfile}}`

- Use REGEX to limit AIDE to a specific string:

`aide {{[-l |--limit=]}}{{REGEX}}`

- Send reporter results to a URL:

`aide {{[-r |--report=]}}{{reporterurl}}`
