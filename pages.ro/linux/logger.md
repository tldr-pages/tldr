# logger

> Adăugați mesaje la syslog (/var/log/syslog).

- Conectaţi un mesaj la syslog:

`logger {{message}}`

- Ia de intrare de la stdin și log la syslog:

`echo {{log_entry}} | logger`

- Trimiteți ieșirea la un server syslog la distanță care rulează la un anumit port. Portul implicit este 514:

`echo {{log_entry}} | logger --server {{hostname}} --port {{port}}`

- Utilizați o etichetă specifică pentru fiecare linie înregistrată. Implicit este numele utilizatorului autentificat:

`echo {{log_entry}} | logger --tag {{tag}}`

- Jurnal mesaje cu o anumită prioritate. Implicit este `user.not`. Consultaţi 'man logger' pentru toate opţiunile de prioritate:

`echo {{log_entry}} | logger --priority {{user.warning}}`
