# setsebool

> Stel de SELinux-boolean-waarde in.
> Zie ook: `semanage boolean`, `getsebool`.
> Meer informatie: <https://manned.org/setsebool>.

- Toon de huidige instelling van [a]lle booleans:

`getsebool -a`

- Stel een boolean tijdelijk in of uit (niet-persistent bij herstart):

`sudo setsebool {{httpd_can_network_connect}} {{1|true|on|0|false|off}}`

- Stel een boolean [P]ersistent in of uit:

`sudo setsebool -P {{container_use_devices}} {{1|true|on|0|false|off}}`

- Stel meerdere booleans tegelijk [P]ersistent in of uit:

`sudo setsebool -P {{key1 1 key2 0 ...}}`

- Stel een boolean persistent in (alternatieve methode met `semanage-boolean`):

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`
