# openrc

> Managerul de servicii OpenRC.
> A se vedea, de asemenea, `rc-status`, `rc-update` și `rc-service`.
> Mai multe informaţii: <https://wiki.gentoo.org/wiki/OpenRC>

- Trecerea la un anumit nivel de execuție:

`sudo openrc {{runlevel_name}}`

- Schimbați la un anumit nivel de execuție, dar nu opriți niciun serviciu existent:

`sudo openrc --no-stop {{runlevel_name}}`
