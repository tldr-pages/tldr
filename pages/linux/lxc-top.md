# lxc-top

> Display resource usage of LXC containers.
> More information: <https://linuxcontainers.org/lxc/manpages/man1/lxc-top.1.html>.

- Start `lxc-top`:

`lxc-top`

- Adjust update interval:

`lxc-top {{[-d|--delay]}} {{5}}`

- Sort by [n]ame, [c]pu use, [b]lock I/O, [m]emory, or [k]ernel memory:

`lxc-top {{[-s|--sort]}} {{n|c|b|m|k}}`
