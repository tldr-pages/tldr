# sntpd

> SNTP-kiszolgáló. Nem szabad manuálisan meghívni. További információ: <https://linux.die.net/man/8/snmpd>.

- Indítsa el a démont:

`sntpd`

- A meglévő állapot felülírása a helyi órával (1. réteg), egy master/primary szerver futtatásához, egy másik (magasabb rétegű) szerverrel való szinkronizálás nélkül:

`sntpd -L`

- Egyéni fájl használata az SNTP állapothoz:

`sntpd -z {{path/to/state.bin}}`
