# wakeonlan

> Send packets to wake-on-LAN (WOL) enabled PCs.
> More information: <https://github.com/jpoliv/wakeonlan>.

- Send packets to all devices on the local network (255.255.255.255) by specifying a MAC address:

`wakeonlan {{01:02:03:04:05:06}}`

- Send packet to a specific device via IP address:

`wakeonlan {{01:02:03:04:05:06}} {{[-i|--ip]}} {{192.168.178.2}}`

- Print the commands, but don't execute them (dry-run):

`wakeonlan {{[-n|--dry-run]}} {{01:02:03:04:05:06}}`

- Run in quiet mode:

`wakeonlan {{[-q|--quiet]}} {{01:02:03:04:05:06}}`
