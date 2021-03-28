# ifup

> Tool used to enable network interfaces.
> More information: <https://manpages.debian.org/jessie/ifupdown/ifup.8.en.html>.

- Enable interface eth0:

`ifup {{eth0}}`

- Enable all the interfaces defined with "auto" in `/etc/network/interfaces`:

`ifup -a`
