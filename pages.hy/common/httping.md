# httping

> Չափել վեբ սերվերի հետաձգումը և թողունակությունը:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/httping>:.

- Ping նշված URL-ը.:

`httping -g {{url}}`

- Ping վեբ սերվերի վրա `host` և `port`:

`httping -h {{host}} -p {{port}}`

- Ping վեբ սերվերի վրա `host`՝ օգտագործելով TLS կապը.:

`httping -l -g https://{{host}}`

- Ping վեբ սերվերը `host`-ի վրա՝ օգտագործելով HTTP հիմնական նույնականացումը.:

`httping -g http://{{host}} -U {{username}} -P {{password}}`
