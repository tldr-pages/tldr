# semanage boolean

> Beheer persistente SELinux-boolean-instellingen.
> Zie ook: `semanage`, `getsebool`, `setsebool`.
> Meer informatie: <https://manned.org/semanage-boolean>.

- Toon alle boolean-instellingen:

`sudo semanage boolean {{[-l|--list]}}`

- Toon alle door de gebruiker gedefinieerde boolean-instellingen zonder koppen:

`sudo semanage boolean {{[-l|--list]}} {{[-C|--locallist]}} {{[-n|--noheading]}}`

- Stel een boolean blijvend in of uit:

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`
