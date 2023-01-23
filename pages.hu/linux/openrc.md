# openrc

> Az OpenRC szolgáltatáskezelő. Lásd még: `rc-status`, `rc-update` és `rc-service`. További információ: <https://wiki.gentoo.org/wiki/OpenRC>.

- Váltás egy adott futási szintre:

`sudo openrc {{runlevel_name}}`

- Váltás egy adott futási szintre, de nem állítja le a meglévő szolgáltatásokat:

`sudo openrc --no-stop {{runlevel_name}}`
