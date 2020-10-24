# physlock

> Lock all consoles and virtual terminals.
> More information: <http://github.com/muennich/physlock>.

- Lock every console (require current user or root to unlock):

`physlock`

- Mute kernel messages on console while locked:

`physlock -m`

- Disable SysRq mechanism while locked:

`physlock -s`

- Display a message before the password prompt:

`physlock -p "{{Locked!}}"`

- Fork and detach physlock (useful for suspend or hibernate scripts):

`physlock -d`
