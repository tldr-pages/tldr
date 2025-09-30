# lshw

> List detailed information about hardware configurations as root user.
> More information: <https://ezix.org/project/wiki/HardwareLiSter>.

- Launch the X11 GUI (if available):

`sudo lshw -X`

- List all hardware in tabular format:

`sudo lshw -short`

- List multiple class of hardware (all disks and storage controllers) in tabular format:

`sudo lshw {{[-c|-class]}} disk {{[-c|-class]}} storage -short`

- Save all network interfaces to an HTML/XML/JSON file:

`sudo lshw {{[-c|-class]}} network -{{html|xml|json}} > interfaces{{.html|.xml|.json}}`

- List network interfaces without revealing sensitive information (IP addresses, serial numbers, etc.):

`sudo lshw {{[-c|-class]}} network -sanitize`

- List a particular class of hardware:

`sudo lshw {{[-c|-class]}} {{system|bridge|memory|processor|address|storage|disk|tape|bus|network|display|input|printer|multimedia|communication|power|volume|generic}}`
