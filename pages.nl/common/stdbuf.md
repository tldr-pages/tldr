# stdbuf

> Voer een commando uit met aangepaste buffering operaties voor de standaard streams.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html>.

- Verander de buffer grootte van `stdin` naar 512 KiB:

`stdbuf {{[-i|--input]}} 512K {{commando}}`

- Verander de buffer van `stdout` naar lijn-buffering:

`stdbuf {{[-o|--output]}} L {{commando}}`

- Verander de buffer van `stderr` naar ongebufferd:

`stdbuf {{[-e|--error]}} 0 {{commando}}`
