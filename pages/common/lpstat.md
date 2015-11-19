# lpstat

> Print cups(common unix printing system) information like available printers and current jobs. 

- Show the system default print destination.

`lpstat -d`

- Display all printer information.

`lpstat -t`

- Show print request status information for a given user.

`lpstat -u {{user}}`

- List printers present on the machine.

`lpstat -p | awk '{print $2}`