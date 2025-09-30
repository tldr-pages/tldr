# ipmitool

> Interface with the Intelligent Platform Management Interface (IPMI).
> More information: <https://manned.org/ipmitool>.

- Start the IPMI driver for local connections:

`systemctl start ipmidrv`

- Open IPMI shell on the local hardware:

`sudo ipmitool shell`

- Open IPMI shell on a remote host:

`ipmitool -H {{ip_address}} -U {{user_name}} shell`
