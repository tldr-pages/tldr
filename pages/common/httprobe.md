# httprobe

> Take a list of domains and probe for working HTTP and HTTPS servers.
> More information: <https://github.com/tomnomnom/httprobe>.

- Probe a list of domains from a text file:

`cat {{input_file}} | httprobe`

- Only check for HTTP if HTTPS is not working:

`cat {{input_file}} | httprobe --prefer-https`

- Probe additional ports with a given protocol:

`cat {{input_file}} | httprobe -p {{https:2222}}`

- Display help:

`httprobe --help`
