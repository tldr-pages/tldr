# lsync

> Transfer files either to or from a remote host (but not between two remote hosts), by default using SSH.
> It is often used to keep two directories on separate systems in sync, ensuring that changes made in one directory are immediately mirrored to the other.
> More information: <https://github.com/lsyncd/lsyncd>.

- Watch the source for changes and run `rsync` to synchronize files to the destination on every change: 

`lsyncd -rsync {{path/to/source}} {{host::share_name}}`

- Lsync with SSH connection:

`lsyncd -rsyncssh {{/home}} {{remotehost.org}} {{backup-home/}}`
