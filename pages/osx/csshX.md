# csshX

> Cluster ssh tool for MacOS.
> More information: <https://github.com/brockgr/csshx>.

- Connect to multiple hosts:

`csshX hostname1 hostname2`

- Connect to multiple hosts with ssh key:

`csshX user@hostname1 user@hostname2 '--ssh_args' '-i /path/to/ssh-key.pem'`

- Connect to pre-defined cluster from /etc/clusters

`csshX cluster1`
