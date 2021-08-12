# etcdctl

> Interfață CLI pentru interacțiunea cu etcd, un magazin de pereche cheie cu valoare ridicată disponibilă.
> Mai multe informaţii: <https://etcd.io/docs/latest/dev-guide/interacting_v3/>

- Afișează valoarea asociată cu o cheie specificată:

`etcdctl get {{my/key}}`

- Stocați o pereche cheie-valoare:

`etcdctl put {{my/key}} {{my_value}}`

- Ștergeți o pereche cheie-valoare:

`etcdctl del {{my/key}}`

- Stocați o pereche cheie-valoare, citirea valorii dintr-un fișier:

`etcdctl put {{my/file}} < {{path/to/file.txt}}`

- Salvați un instantaneu al tastaturii etcd:

`etcdctl snapshot save {{path/to/snapshot.db}}`

- Restaurați un instantaneu al unui keystore etcd (reporniți serverul etcd după aceea):

`etcdctl snapshot restore {{path/to/snapshot.db}}`

- Adaugă un utilizator:

`etcdctl user add {{my_user}}`

- Urmăriți o cheie pentru schimbări:

`etcdctl watch {{my/key}}`
