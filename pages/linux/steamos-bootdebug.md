# steamos-bootdebug

> Manage the SteamOS boot process.
> More information: <https://gitlab.com/users/evlaV/projects>.

- Change what SteamOS shows on boot:

`sudo steamos-bootdebug {{kernel-debug|kernel-quiet|menu|verbose|quiet|status}}`

- Show kernel logging only on the next boot:

`sudo steamos-bootdebug {{kernel-debug-once}}`

- Set if the boot process should log to a file:

`sudo steamos-bootdebug log {{enable|disable}}`

- Display the recorded log file:

`sudo steamos-bootdebug log show`
