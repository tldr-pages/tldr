# լոբի ցողուն

> Պարզ և ընդհանուր աշխատանքային հերթի սերվեր:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/beanstalkd>:.

- Գործարկեք սերվերը, լսելով 11300 նավահանգստում.:

`beanstalkd`

- [l]լսել կոնկրետ [p]պորտում և հասցեում՝:

`beanstalkd -l {{ip_address}} -p {{port_number}}`

- Պահպանեք աշխատանքային հերթերը՝ դրանք պահելով սկավառակի վրա.:

`beanstalkd -b {{path/to/persistence_directory}}`

- Համաժամեցեք համառության գրացուցակի հետ յուրաքանչյուր 500 միլիվայրկյան:

`beanstalkd -b {{path/to/persistence_directory}} -f {{500}}`
