# ifup

> Enable network interfaces.
> More information: <https://manned.org/ifup.8>.

- Enable interface eth0:

`ifup {{eth0}}`

- Enable all the interfaces defined with "auto" in `/etc/network/interfaces`:

`ifup {{[-a|--all]}}`
