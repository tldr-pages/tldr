# sccache

> A fast C/C++/Rust compiler cache.
> Composed of a client and a server, both running on the machine.
> More information: <https://manned.org/sccache>.

- Show compilation statistics:

`sccache {{[-s|--show-stats]}}`

- Run `gcc` (or any compiler command) through `sccache`:

`sccache gcc {{path/to/file.c}}`

- Start `sccache` server in the foreground and print logs:

`sccache --stop-server; SCCACHE_LOG=trace SCCACHE_START_SERVER=1 SCCACHE_NO_DAEMON=1 sccache`

- Ask scheduler for distributed compilation status:

`sccache --dist-status`
