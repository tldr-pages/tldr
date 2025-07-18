# nmcli general

> Manage general settings of NetworkManager.
> More information: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html>.

- Show the general status of NetworkManager:

`nmcli {{[g|general]}}`

- Show the hostname of the current device:

`nmcli {{[g|general]}} {{[h|hostname]}}`

- Change the hostname of the current device:

`sudo nmcli {{[g|general]}} {{[h|hostname]}} {{new_hostname}}`

- Show the permissions of NetworkManager:

`nmcli {{[g|general]}} {{[p|permissions]}}`

- Show the current logging level and domains:

`nmcli {{[g|general]}} {{[l|logging]}}`

- Set the logging level and/or domains (see `man NetworkManager.conf` for all available domains):

`sudo nmcli {{[g|general]}} {{[l|logging]}} {{[l|level]}} {{INFO|OFF|ERR|WARN|DEBUG|TRACE}} domain {{domain_1,domain_2,...}}`
