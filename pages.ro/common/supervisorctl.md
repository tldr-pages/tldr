# supervisorctl

> Supervisor este un sistem client/server care permite utilizatorilor săi să controleze un număr de procese pe sisteme de operare asemănătoare UNIX.
> Supervisorctl este piesa client linia de comandă a supervizorului, care oferă o interfață asemănătoare cochilii.
> Mai multe informaţii: <http://supervisord.org>

- Pornește/oprește/repornește un proces:

`supervisorctl {{start|stop|restart}} {{process_name}}`

- Pornește/oprește/repornește toate procesele dintr-un grup:

`supervisorctl {{start|stop|restart}} {{group_name}}:*`

- Arată ultima 100 **octeți** de proces stderr:

`supervisorctl tail -100 {{process_name}} stderr`

- Păstrați afișarea stdout unui proces:

`supervisorctl tail -f {{process_name}} stdout`

- Reîncărcați fișierul de configurare proces pentru a adăuga/elimina procesele după cum este necesar:

`supervisorctl update`
