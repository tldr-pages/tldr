# notifyd

> Értesítési kiszolgáló. Nem szabad manuálisan meghívni. További információ: <https://www.manpagez.com/man/8/notifyd/>.

- Indítsa el a démont:

`notifyd`

- Naplózza a hibakeresési üzeneteket az alapértelmezett naplófájlba (`/var/log/notifyd.log`):

`notifyd -d`

- Naplózza a hibakeresési üzeneteket egy másik naplófájlba:

`notifyd -d -log_file {{path/to/log}}`
