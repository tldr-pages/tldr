# etcd

> Egy elosztott rendszer legkritikusabb adatainak elosztott, megbízható kulcs-érték tárolója. További információ: <https://etcd.io>.

- Indítson el egy egycsomópontos etcd fürtöt:

`etcd`

- Egyetlen csomópontból álló etcd fürt indítása, amely egy egyéni URL-címen hallgatja az ügyfélkéréseket:

`etcd --advertise-client-urls {{http://127.0.0.1:1234}} --listen-client-urls {{http://127.0.0.1:1234}}`

- Indítson el egy egycsomópontos etcd fürtöt egy egyéni névvel:

`etcd --name {{my_etcd_cluster}}`

- Indítson el egy egycsomópontos etcd fürtöt a http://localhost:2379/debug/pprof/ címen elérhető átfogó metrikákkal:

`etcd --enable-pprof --metrics extensive`
