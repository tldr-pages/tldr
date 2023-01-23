# rfkill

> A vezeték nélküli eszközök engedélyezése és letiltása. További információ: <https://manned.org/rfkill>.

- Eszközök listázása:

`rfkill`

- Szűrés oszlopok szerint:

`rfkill -o {{ID,TYPE,DEVICE}}`

- Eszközök blokkolása típus szerint (pl. bluetooth, wlan):

`rfkill block {{bluetooth}}`

- Eszközök blokkolásának feloldása típusonként (pl. bluetooth, wlan):

`rfkill unblock {{wlan}}`

- Kimenet JSON formátumban:

`rfkill -J`
