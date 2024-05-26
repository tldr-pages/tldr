# torify

> Route network traffic through the Tor network.
> More information: <https://manned.org/man/torify>.

- Route traffic via Tor:

`torify {{command}}`

- Toggle Tor in shell:

`torify {{on|off}}`

- Spawn a Tor-enabled shell:

`torify --shell`

- Check for a Tor-enabled shell:

`torify show`

- Specify Tor configuration file:

`torify -c {{config-file}} {{command}}`

- Use a specific Tor SOCKS proxy:

`torify -P {{proxy}} {{command}}`

- Redirect output to a file:

`torify {{command}} > {{path/to/output}}`
