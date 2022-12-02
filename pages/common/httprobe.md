# httprobe

> Take a list of domains and probe for working HTTP and HTTPS servers.
> More information: <https://github.com/tomnomnom/httprobe>.

- Probe a list of domains from a text file:

`cat {{path/to/file}} | httprobe`

- Only check for HTTP if HTTPS is not working:

`cat {{path/to/file}} | httprobe --prefer-https`

- Probe additional ports with a given protocol:

`cat {{path/to/file}} | httprobe -p {{https:2222}}`

- Output all available options:

`httprobe --help`
