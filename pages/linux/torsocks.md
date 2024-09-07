# torsocks

> Route the traffic of any application through the Tor network.
> Note: `torsocks` will assume that it should connect to the Tor SOCKS proxy running at 127.0.0.1:9050 being the defaults of the Tor daemon.
> More information: <https://gitlab.torproject.org/tpo/core/torsocks/>.

- Run a command using Tor:

`torsocks {{command}}`

- Enable or disable Tor in this shell:

`. torsocks {{on|off}}`

- Spawn a new Tor enabled shell:

`torsocks --shell`

- Check if current shell is Tor enabled (`LD_PRELOAD` value will be empty if disabled):

`torsocks show`

- [i]solate traffic through a different Tor circuit, improving anonymity:

`torsocks --isolate {{curl https://check.torproject.org/api/ip}}`

- Connect to a Tor proxy running on a specific [a]ddress and [P]ort:

`torsocks --address {{ip}} --port {{port}} {{command}}`
