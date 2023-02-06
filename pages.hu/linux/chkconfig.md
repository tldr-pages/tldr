# chkconfig

> A szolgáltatások futtatási szintjének kezelése a CentOS 6 rendszeren. További információ: <https://manned.org/chkconfig>.

- Szolgáltatások listázása runlevelekkel:

`chkconfig --list`

- Megjeleníti egy szolgáltatás futási szintjét:

`chkconfig --list {{ntpd}}`

- A szolgáltatás engedélyezése indításkor:

`chkconfig {{sshd}} on`

- Engedélyezze a szolgáltatás indításkor a 2., 3., 4. és 5. futási szintek esetén:

`chkconfig --level {{2345}} {{sshd}} on`

- A szolgáltatás letiltása indításkor:

`chkconfig {{ntpd}} off`

- A szolgáltatás letiltása indításkor a 3. futási szint esetén:

`chkconfig --level {{3}} {{ntpd}} off`
