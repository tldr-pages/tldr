# psd

> Profile-sync-daemon: manages and synchronizes browser profiles in tmpfs (RAM).
> More information: <https://github.com/graysky2/profile-sync-daemon>.

- Parse configuration and preview which profiles will be managed:

`psd preview`

- Clean and delete all crash recovery snapshots:

`psd clean`

- Start the daemon and synchronize browser profiles via systemd:

`systemctl --user start psd.service`

- Enable the daemon to start automatically at login:

`systemctl --user enable psd.service`

- Check the status of the background synchronization daemon:

`systemctl --user status psd.service`
