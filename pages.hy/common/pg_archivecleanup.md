# pg_արխիվային մաքրում

> Հեռացրեք հին WAL արխիվային ֆայլերը PostgreSQL-ում:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/pgarchivecleanup.html>:.

- Մաքրել արխիվային գրացուցակը մինչև տվյալ WAL ֆայլը.:

`pg_archivecleanup {{path/to/archive}} {{path/to/walfile}}`

- Կատարեք չոր գործարկում (թվարկեք ֆայլերը, որոնք կհեռացվեն առանց իրականում դա անելու).:

`pg_archivecleanup {{[-n|--dry-run]}} {{path/to/archive}} {{path/to/walfile}}`

- Հեռացրեք ֆայլի ընդլայնումը նախքան ջնջումը որոշելը.:

`pg_archivecleanup {{[-x|--strip-extension]}} {{extension}} {{path/to/archive}} {{path/to/walfile}}`

- Հեռացրեք նաև պահուստային պատմության ֆայլերը.:

`pg_archivecleanup {{[-b|--clean-backup-history]}} {{path/to/archive}} {{path/to/walfile}}`

- Միացնել վրիպազերծման գրանցման ելքը.:

`pg_archivecleanup {{[-d|--debug]}} {{path/to/archive}} {{path/to/walfile}}`
