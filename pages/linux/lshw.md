# lshw

> List detailed information about hardware configurations as root user.

- Launch the GUI:

`sudo lshw -X`

- List all hardwares with table format:

`sudo lshw -short`

- List all disks and storage controllers with table format:

`sudo lshw -class disk -class storage -short`

- Save all network interfaces to HTML file:

`sudo lshw -class network -html > {{interfaces.html}}`
