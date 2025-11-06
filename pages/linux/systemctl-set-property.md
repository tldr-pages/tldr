# systemctl set-property

> Set the specified unit properties at runtime.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#set-property%20UNIT%20PROPERTY=VALUE%E2%80%A6>.

- Set a property for a running service:

`systemctl set-property {{unit}} {{property}}={{value}}`

- Set multiple properties at once:

`systemctl set-property {{unit}} {{property_1=value_1 property_2=value_2 ...}}`

- Set a property only for the current runtime session (not persistent):

`systemctl set-property --runtime {{unit}} {{property}}={{value}}`

- Reset a property to its default value:

`systemctl set-property {{unit}} {{property}}=`

- Reset multiple properties to its default values:

`systemctl set-property {{unit}} {{property_1= property_2= ...}}`
