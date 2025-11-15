# ipmitool

> Interface met de Intelligent Platform Management Interface (IPMI).
> Meer informatie: <https://man.freebsd.org/cgi/man.cgi?query=ipmitool>.

- Laad de IPMI kernelmodule voor lokale verbindingen:

`kldload ipmi.ko`

- Open de IPMI shell op de lokale hardware:

`ipmitool shell`

- Open IPMI shell op een remote host:

`ipmitool -H {{ip_adres}} -U {{gebruikersnaam}} shell`
