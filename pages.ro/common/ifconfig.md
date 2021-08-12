# ifconfig

> Configurator de interfață de rețea.
> Mai multe informaţii: <https://net-tools.sourceforge.io/man/ifconfig.8.html>

- Vizualizați setările de rețea ale unui adaptor ethernet:

`ifconfig eth0`

- Afișarea detaliilor tuturor interfețelor, inclusiv a interfețelor dezactivate:

`ifconfig -a`

- Dezactivați interfața eth0:

`ifconfig eth0 down`

- Activați interfața eth0:

`ifconfig eth0 up`

- Alocați adresa IP interfeței eth0:

`ifconfig eth0 {{ip_address}}`
