# etcdctl

> Փոխազդեք `etcd`-ի հետ, որը շատ մատչելի բանալի-արժեք զույգ խանութ է:.
> Լրացուցիչ տեղեկություններ. <https://etcd.io/docs/latest/dev-guide/interacting_v3/>:.

- Ցուցադրել նշված բանալի հետ կապված արժեքը.:

`etcdctl get {{my/key}}`

- Պահպանեք բանալի-արժեք զույգ.:

`etcdctl put {{my/key}} {{my_value}}`

- Ջնջել բանալի-արժեք զույգը.:

`etcdctl del {{my/key}}`

- Պահպանեք բանալի-արժեք զույգ՝ կարդալով արժեքը ֆայլից.:

`etcdctl < {{path/to/file.txt}} put {{my/file}}`

- Պահպանեք etcd keystore-ի լուսանկարը.:

`etcdctl snapshot save {{path/to/snapshot.db}}`

- Վերականգնել etcd keystore-ի լուսանկարը (հետագայում վերագործարկեք etcd սերվերը).:

`etcdctl snapshot restore {{path/to/snapshot.db}}`

- Ավելացնել օգտվող.:

`etcdctl user add {{my_user}}`

- Դիտեք փոփոխությունների բանալին.:

`etcdctl watch {{my/key}}`
