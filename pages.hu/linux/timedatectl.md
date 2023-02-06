# timedatectl

> A rendszeridő és a dátum ellenőrzése. További információ: <https://manned.org/timedatectl>.

- A rendszer aktuális óraidejének ellenőrzése:

`timedatectl`

- A rendszeróra helyi idejének közvetlen beállítása:

`timedatectl set-time "{{yyyy-MM-dd hh:mm:ss}}"`

- Az elérhető időzónák listája:

`timedatectl list-timezones`

- A rendszer időzónájának beállítása:

`timedatectl set-timezone {{timezone}}`

- Network Time Protocol (NTP) szinkronizáció engedélyezése:

`timedatectl set-ntp on`

- A hardveróra időszabványának helyi időre történő módosítása:

`timedatectl set-local-rtc 1`
