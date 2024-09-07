# autorecon

> A multi-threaded network reconnaissance tool which performs automated enumeration of services.
> More information: <https://github.com/Tib3rius/AutoRecon>.

- Perform reconnaissance on target host(s) (detailed scan results will be dumped in `./results`):

`sudo autorecon {{host_or_ip1,host_or_ip2,...}}`

- Perform reconnaissance on [t]arget(s) from a file:

`sudo autorecon --target-file {{path/to/file}}`

- [o]utput results to a different directory:

`sudo autorecon --output {{path/to/results}} {{host_or_ip1,host_or_ip2,...}}`

- Limit scanning to specific [p]orts and protocols (`T` for TCP, `U` for UDP, `B` for both):

`sudo autorecon --ports {{T:21-25,80,443,U:53,B:123}} {{host_or_ip1,host_or_ip2,...}}`
