# scutil

> Manage system configuration parameters.
> Require root privileges when setting configuration.
> More information: <https://keith.github.io/xcode-man-pages/scutil.8.html>.

- Display DNS Configuration:

`scutil --dns`

- Display proxy configuration:

`scutil --proxy`

- Get computer name:

`scutil --get ComputerName`

- Set computer name:

`sudo scutil --set ComputerName {{computer_name}}`

- Get hostname:

`scutil --get HostName`

- Set hostname:

`scutil --set HostName {{hostname}}`
