# nmcli general

> Manage general settings of NetworkManager.
> More information: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Show the general status of NetworkManager:

`nmcli {{[g|general]}}`

- Show the hostname of the current device:

`nmcli {{[g|general]}} hostname`

- Change the hostname of the current device:

`sudo nmcli {{[g|general]}} hostname {{new_hostname}}`

- Show the permissions of NetworkManager:

`nmcli {{[g|general]}} permissions`

- Show the current logging level and domains:

`nmcli {{[g|general]}} logging`

- Set the logging level and/or domains (see `man NetworkManager.conf` for all available domains):

`nmcli {{[g|general]}} logging level {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{domain_1,domain_2,...}}`
