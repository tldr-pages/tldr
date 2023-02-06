# csshX

> Cluster SSH eszköz macOS-hez. További információ: <https://github.com/brockgr/csshx>.

- Csatlakozás több állomáshoz:

`csshX {{hostname1}} {{hostname2}}`

- Csatlakozás több állomáshoz egy adott SSH-kulccsal:

`csshX {{user@hostname1}} {{user@hostname2}} --ssh_args "-i {{path/to/ssh_key.pem}}"`

- Csatlakozás egy előre meghatározott fürthöz a `/etc/clusters` oldalon:

`csshX cluster1`
