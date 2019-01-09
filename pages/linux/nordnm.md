# nordnm

> This tool automates the importing and secures the usage of NordVPN OpenVPN configurations through Network Manager.

- View available categories and countries:

`sudo nordnm list --categories --countries`

- Synchronise, update configuration files, activate the kill-switch and auto-connect to a "normal" UDP server in the US:

`sudo nordnm sync -uka us normal udp`

- View metrics of the synchronised servers:

`sudo nordnm list --active-servers`

- Set your MAC address to be randomised each time you connect to a network:

`sudo nordnm mac --random`

- Change the auto-connect to another synchronised server:

`sudo nordnm -a ru p2p udp`

- Update the settings:

`sudo nordnm update --settings`

- Update the user credentials:

`sudo nordnm update --credentials`

- Remove all settings and files:

`sudo nordnm remove --all`
