# physlock

> Lock all consoles / virtual terminals.
> More information: http://github.com/muennich/physlock.

- Lock every console (require current user or root to unlock):

`physlock`

- Mute kernel messages on console while locked:

`physlock -m`

- Disable SysRq mechanism while locked:

`physlock -s`

- Display message before the password prompt:

`physlock -p {{"Locked!"}}`

- Fork and detach physlock, so it can be used in suspend/hibernate scripts:

`physlock -d`
