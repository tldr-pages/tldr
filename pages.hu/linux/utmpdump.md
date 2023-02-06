# utmpdump

> A btmp, utmp és wtmp könyvelési fájlok kitöltése és betöltése. További információ: <https://manned.org/utmpdump>.

- A `/var/log/wtmp` fájl dumpolása a standard kimenetre egyszerű szövegként:

`utmpdump {{/var/log/wtmp}}`

- Egy korábban dömbbölt fájl betöltése a `/var/log/wtmp` címre:

`utmpdump -r {{dumpfile}} > {{/var/log/wtmp}}`
