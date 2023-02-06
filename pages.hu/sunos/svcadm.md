# svcadm

> A szolgáltatáspéldányok kezelése. További információ: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Egy szolgáltatás engedélyezése a szolgáltatás-adatbázisban:

`svcadm enable {{service_name}}`

- A szolgáltatás letiltása:

`svcadm disable {{service_name}}`

- Egy futó szolgáltatás újraindítása:

`svcadm restart {{service_name}}`

- Parancs a szolgáltatásnak a konfigurációs fájlok újraolvasására:

`svcadm refresh {{service_name}}`

- Egy szolgáltatás törlése a karbantartási állapotból, és indítási parancs kiadása:

`svcadm clear {{service_name}}`
