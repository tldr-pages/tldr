# getsebool

> Toon de SELinux-boolean-waarde.
> Zie ook: `semanage boolean`, `setsebool`.
> Meer informatie: <https://manned.org/getsebool>.

- Toon de huidige instelling van een boolean:

`getsebool {{httpd_can_connect_ftp}}`

- Toon de huidige instelling van [a]lle booleans:

`getsebool -a`

- Toon de huidige instelling van alle booleans met toelichting:

`sudo semanage boolean {{[-l|--list]}}`
