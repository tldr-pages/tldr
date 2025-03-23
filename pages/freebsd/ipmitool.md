# ipmitool

> Interface with the Intelligent Platform Management Interface (IPMI).
> More information: <https://man.freebsd.org/cgi/man.cgi?query=ipmitool>.

- Load the IPMI kernel module:

`kldload ipmi.ko`

- Open ipmi shell on the local hardware :

`ipmitool shell`

- Open ipmi shell on a remote host:

`ipmitool -H {{ip_address}} -U {{user_name}} shell`
