# etcdctl

> CLI interface for interacting with etcd high performance key/value pair store.
> Etcd stores keys in a filesystem-like format, e.g. /my/key.
> More information: <https://etcd.io/docs/latest/dev-guide/interacting_v3/>.

- Get a key:

`etcdctl get {{my/key}}`

- Set a key:

`etcdctl put {{my/key}} {{my_value}}`

- Delete a key:

`etcdctl del {{my/key}}`

- Set a key, reading the value from a file:

`etcdctl put {{my/file}} < {{path/to/file.txt}}`

- Save a snapshot of the etcd keystore:

`etcdctl snapshot save {{path/to/snapshot.db}}`

- Restore a snapshot of an etcd keystore (restart the etcd server afterwards):

`etcdctl snapshot restore {{path/to/snapshot.db}}`

- Add a user:

`etcdctl user add {{my_user}}`

- Watch a key for changes:

`etcdctl watch {{my/key}}`
