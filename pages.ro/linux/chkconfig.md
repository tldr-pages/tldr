# chkconfig

> Gestionați nivelul de execuție al serviciilor pe CentOS 6.
> Mai multe informaţii: <https://manned.org/chkconfig>

- Lista serviciilor cu nivel de execuție:

`chkconfig --list`

- Afișează nivelul de execuție al unui serviciu:

`chkconfig --list {{ntpd}}`

- Activați serviciul la boot:

`chkconfig {{sshd}} on`

- Activează serviciul la pornire pentru nivelurile de execuție 2, 3, 4 și 5:

`chkconfig --level {{2345}} {{sshd}} on`

- Dezactivați serviciul la boot:

`chkconfig {{ntpd}} off`

- Dezactivează serviciul la boot pentru nivelul de execuție 3:

`chkconfig --level {{3}} {{ntpd}} off`
