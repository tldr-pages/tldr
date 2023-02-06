# ntpdate

> A dátum és az idő szinkronizálása és beállítása NTP-n keresztül. További információ: <http://support.ntp.org/documentation>.

- A dátum és az idő szinkronizálása és beállítása:

`sudo ntpdate {{host}}`

- Az idő beállítása nélkül lekérdezi a hosztot:

`ntpdate -q {{host}}`

- Használjon nem privilegizált portot, ha a tűzfal blokkolja a privilegizált portokat:

`sudo ntpdate -u {{host}}`

- Kényszerítse az idő lépcsőzését a `settimeofday` használatával a `slewed` helyett:

`sudo ntpdate -b {{host}}`
