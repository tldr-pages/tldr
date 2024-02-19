# ifup

> Enable network interfaces.
> More information: <https://manpages.debian.org/latest/ifupdown/ifup.8.html>.

- Enable interface eth0:

`ifup {{eth0}}`

- Enable all the interfaces defined with "auto" in `/etc/network/interfaces`:

`ifup -a`
