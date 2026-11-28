# kbdinfo

> Display information about keyboard settings and virtual console modes.
> More information: <https://manned.org/kbdinfo>.

- Show the current virtual console mode:

`kbdinfo getmode`

- Check whether the virtual console is in text mode (returns an exit status):

`kbdinfo getmode text`

- Show the current keyboard mode:

`kbdinfo gkbmode`

- Check whether the keyboard is using Unicode mode:

`kbdinfo gkbmode unicode`

- Show the current Meta key handling mode:

`kbdinfo gkbmeta`

- Show the current Caps Lock, Num Lock, and Scroll Lock states:

`kbdinfo gkbled`

- Get keyboard information from a specific console:

`kbdinfo -C {{/dev/ttyN}} {{getmode|gkbmode|gkbmeta|gkbled}}`
