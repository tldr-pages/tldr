#հանգույց

> Վերահսկիչ հանգույց DNS սերվեր:.
> Լրացուցիչ տեղեկություններ. <https://www.knot-dns.cz/docs/latest/html/man_knotc.html>:.

- Սկսեք խմբագրել գոտի.:

`knotc zone-begin {{zone}}`

- Սահմանեք A ռեկորդ TTL-ով 3600:

`knotc zone-set {{zone}} {{subdomain}} 3600 A {{ip_address}}`

- Ավարտեք գոտու խմբագրումը.:

`knotc zone-commit {{zone}}`

- Ստացեք ընթացիկ գոտու տվյալները.:

`knotc zone-read {{zone}}`

- Ստացեք ընթացիկ սերվերի կոնֆիգուրացիան.:

`knotc conf-read server`
