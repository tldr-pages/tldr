# scutil

> Manage system configuration parameters
> Necessitates to be root when setting configuration

- Displays DNS Configuration

`scutil --dns`

- Displays proxy configuration

`scutil --proxy`

- Get/Set computer name

`scutil --get ComputerName`

`sudo scutil --set ComputerName {{computer_name}}`

- Get/Set Hostname

`scutil --get HostName`

`scutil --set HostName {{hostname}}`
