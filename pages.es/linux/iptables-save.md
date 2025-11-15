# iptables-save

> Guarda la configuración IPv4 de `iptables`.
> Use `ip6tables-save` para hacer lo mismo para IPv6.
> Más información: <https://manned.org/iptables-save>.

- Imprime la configuración de `iptables`:

`sudo iptables-save`

- Imprime la configuración de `iptables` de una [t]abla específica:

`sudo iptables-save {{[-t|--table]}} {{tabla}}`

- Guarda la configuración de `iptables` al archivo:

`sudo iptables-save {{[-f|--file]}} {{ruta/al/archivo}}`
