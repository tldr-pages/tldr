# etcd

> Un magazin distribuit, fiabil, cu valoare cheie pentru cele mai critice date ale unui sistem distribuit.
> Mai multe informaţii: <https://etcd.io>

- Porniți un cluster etcd cu un singur nod:

`etcd`

- Porniți un cluster etcd cu un singur nod, ascultând solicitările clienților pe un URL personalizat:

`etcd --advertise-client-urls {{http://127.0.0.1:1234}} --listen-client-urls {{http://127.0.0.1:1234}}`

- Porniți un cluster etcd cu un singur nod cu un nume personalizat:

`etcd --name {{my_etcd_cluster}}`

- Porniți un cluster etcd cu un singur nod, cu valori extinse disponibile la http://localhost:2379/debug/pprof/:

`etcd --enable-pprof --metrics extensive`
