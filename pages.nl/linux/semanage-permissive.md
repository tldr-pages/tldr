# semanage permissive

> Beheer persistente SELinux permissieve domeinen.
> Let op dat dit het proces effectief onbeperkt maakt. Voor langdurig gebruik wordt aanbevolen om SELinux correct te configureren.
> Zie ook: `semanage`, `getenforce`, `setenforce`.
> Meer informatie: <https://manned.org/semanage-permissive>.

- Toon alle procestypen (ook wel domeinen genoemd) die in permissieve modus zijn:

`sudo semanage permissive {{[-l|--list]}}`

- Stel de permissieve modus in voor een domein:

`sudo semanage permissive {{[-a|--add]}} {{httpd_t}}`

- Zet de permissieve modus uit voor een domein:

`sudo semanage permissive {{[-d|--delete]}} {{httpd_t}}`
