# semanage boolean

> Beheer persistente SELinux-boolean-instellingen.
> Zie ook: `semanage` voor het beheren van SELinux-beleid, `getsebool` voor het controleren van boolean-waarden, en `setsebool` voor het toepassen van niet-blijvende boolean-instellingen.
> Meer informatie: <https://manned.org/semanage-boolean>.

- Toon alle boolean-instellingen:

`sudo semanage boolean {{[-l|--list]}}`

- Toon alle door de gebruiker gedefinieerde boolean-instellingen zonder koppen:

`sudo semanage boolean {{[-l|--list]}} {{[-C|--locallist]}} {{[-n|--noheading]}}`

- Stel een boolean blijvend in of uit:

`sudo semanage boolean {{[-m|--modify]}} {{-1|--on|-0|--off}} {{haproxy_connect_any}}`
