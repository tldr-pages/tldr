# ipmitool

> Interface with the Intelligent Platform Management Interface (IPMI).
> More information: <https://man.freebsd.org/cgi/man.cgi?query=ipmitool>.

- Load the IPMI kernel module for local connections:

`kldload ipmi.ko`

- Open IPMI shell on the local hardware:

`ipmitool shell`

- Open IPMI shell on a remote host:

`ipmitool -H {{ip_address}} -U {{user_name}} shell`
