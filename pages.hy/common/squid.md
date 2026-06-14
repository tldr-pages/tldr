# կաղամար

> Քեշավորել և փոխանցել HTTP հարցումները պրոքսի սերվերի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/squid>:.

- Սկսեք Squid-ը հետին պլանում.:

`sudo squid`

- Սկսեք Squid-ը առաջին պլանում.:

`sudo squid -N`

- Սկսեք Squid-ը հատուկ կազմաձևման ֆայլով.:

`sudo squid -f {{path/to/squid.conf}}`

- Ստուգեք կազմաձևման ֆայլը սխալների համար.:

`sudo squid -k parse`

- Վերբեռնեք կազմաձևման ֆայլը.:

`sudo squid -k reconfigure`

- Փակեք Squid-ը նրբագեղորեն.:

`sudo squid -k shutdown`

- Պտտեցնել գրանցամատյանի ֆայլերը.:

`sudo squid -k rotate`
