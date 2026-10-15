# psd

> Profile-sync-daemon: keep browser profiles in RAM (tmpfs) and sync them back to disk periodically.
> More information: <https://manned.org/psd>.

- Show what psd will do or is doing ([p]review mode):

`psd p`

- Delete all crash recovery snapshots ([c]lean mode):

`psd c`

- Start psd for the current user:

`systemctl --user start psd`

- Enable psd to start on login:

`systemctl --user enable psd`

- Edit the config file:

`$EDITOR ~/.config/psd/psd.conf`
