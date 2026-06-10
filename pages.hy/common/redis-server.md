# redis-server

> Մշտական բանալի-արժեքի տվյալների բազա:.
> Լրացուցիչ տեղեկություններ. <https://redis.io/tutorials/operate/redis-at-scale/talking-to-redis/configuring-a-redis-server/>:.

- Սկսեք Redis սերվերը, օգտագործելով լռելյայն պորտը (6379) և գրեք գրանցամատյանները `stdout`-ում:

`redis-server`

- Սկսեք Redis սերվերը, օգտագործելով լռելյայն նավահանգիստը, որպես ֆոնային գործընթաց.:

`redis-server --daemonize yes`

- Սկսեք Redis սերվերը, օգտագործելով նշված նավահանգիստը, որպես ֆոնային գործընթաց.:

`redis-server --port {{port}} --daemonize yes`

- Սկսեք Redis սերվերը հատուկ կազմաձևման ֆայլով.:

`redis-server {{path/to/redis.conf}}`

- Սկսեք Redis սերվերը մանրամասն գրանցմամբ.:

`redis-server --loglevel {{warning|notice|verbose|debug}}`
