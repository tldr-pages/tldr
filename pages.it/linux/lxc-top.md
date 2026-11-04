# lxc-top

> Mostra l'uso delle risorse dei container LXC.
> Maggiori informazioni: <https://linuxcontainers.org/lxc/manpages/man1/lxc-top.1.html>.

- Avvia `lxc-top`:

`lxc-top`

- Regola l'intervallo di aggiornamento:

`lxc-top {{[-d|--delay]}} {{5}}`

- Ordina per [n]ome, uso [c]pu, [b]lock I/O, [m]emoria o [k]ernel memory:

`lxc-top {{[-s|--sort]}} {{n|c|b|m|k}}`
