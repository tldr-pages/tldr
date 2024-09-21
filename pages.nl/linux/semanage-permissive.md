# semanage permissive

> Beheer persistente SELinux permissieve domeinen.
> Let op dat dit het proces effectief onbeperkt maakt. Voor langdurig gebruik wordt aanbevolen om SELinux correct te configureren.
> Zie ook: `semanage`, `getenforce`, `setenforce`.
> Meer informatie: <https://manned.org/semanage-permissive>.

- Toon alle procestypen (ook wel domeinen genoemd) die in permissieve modus zijn:

`sudo semanage permissive {{-l|--list}}`

- Stel de permissieve modus in of uit voor een domein:

`sudo semanage permissive {{-a|--add|-d|--delete}} {{httpd_t}}`
