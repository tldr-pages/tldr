# pathchk

> Egy vagy több elérési útvonal érvényességének és hordozhatóságának ellenőrzése. További információ: <https://www.gnu.org/software/coreutils/pathchk>.

- Az elérési utak érvényességének ellenőrzése az aktuális rendszerben:

`pathchk {{path1 path2 …}}`

- Az elérési utak érvényességének ellenőrzése a POSIX-kompatibilis rendszerek szélesebb körében:

`pathchk -p {{path1 path2 …}}`

- Az elérési utak érvényességének ellenőrzése az összes POSIX-kompatibilis rendszeren:

`pathchk --portability {{path1 path2 …}}`

- Csak az üres elérési utak vagy az élen álló kötőjelek (-) ellenőrzése:

`pathchk -P {{path1 path2 …}}`
