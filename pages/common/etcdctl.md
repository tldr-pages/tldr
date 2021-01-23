# etcdctl

> CLI interface for interacting with `etcd`, a highly-available key-value pair store.
> Etcd stores data in hierarchically organized directories, as in a standard filesystem.
> More information: <https://etcd.io/docs/latest/dev-guide/interacting_v3/>.

- Display the value associated with a specified key:

`etcdctl get {{my/key}}`

- Store a key-value pair:

`etcdctl put {{my/key}} {{my_value}}`

- Delete a key-value pair:

`etcdctl del {{my/key}}`

- Store a key-value pair, reading the value from a file:

`etcdctl put {{my/file}} < {{path/to/file.txt}}`

- Save a snapshot of the etcd keystore:

`etcdctl snapshot save {{path/to/snapshot.db}}`

- Restore a snapshot of an etcd keystore (restart the etcd server afterwards):

`etcdctl snapshot restore {{path/to/snapshot.db}}`

- Add a user:

`etcdctl user add {{my_user}}`

- Watch a key for changes:

`etcdctl watch {{my/key}}`
