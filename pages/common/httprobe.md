# httprobe

> Take a list of domains and probe for working HTTP and HTTPS servers.
> More information: <https://github.com/tomnomnom/httprobe>.

- Probe a list of domains from a text file:

`httprobe < {{input_file}}`

- Only check for HTTP if HTTPS is not working:

`httprobe --prefer-https < {{input_file}}`

- Probe additional ports with a given protocol:

`httprobe -p {{https:2222}} < {{input_file}}`

- Display help:

`httprobe --help`
