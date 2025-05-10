# lshw

> List detailed information about hardware configurations as root user.
> More information: <https://manned.org/lshw>.

- Launch the GUI:

`sudo lshw -X`

- List all hardware in tabular format:

`sudo lshw -short`

- List all disks and storage controllers in tabular format:

`sudo lshw {{[-c|-class]}} disk -class storage -short`

- Save all network interfaces to an HTML/XML/JSON file:

`sudo lshw {{[-c|-class]}} network -{{html|xml|json}} > {{interfaces.html|interfaces.xml|interfaces.json}}`
