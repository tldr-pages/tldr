# ipmitool

> Interface with the Intelligent Platform Management Interface (IPMI).
> More information: <https://manned.org/ipmitool>.

- Start the IPMI driver for local connections:

`systemctl start ipmidrv`

- Open ipmi shell on the local hardware :

`sudo ipmitool shell`

- Open ipmi shell on a remote host:

`ipmitool -H {{ip_address}} -U {{user_name}} shell`
