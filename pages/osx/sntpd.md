# sntpd

> An SNTP server.
> It should not be invoked manually.

- Start the daemon:

`sntpd`

- Overwrite existing state with the local clock (stratum 1), for running a master/primary server, without synchronizing with another (higher stratum) server:

`sntpd -L`

- Use a custom file for the SNTP state:

`sntpd -z {{path/to/state.bin}}`
