# ifconfig

> Configure and show the parameters of a wireless network interface.
> More information: <https://linux.die.net/man/8/iwconfig>.

- Show the parameters and statistics of all the interfaces:

`iwconfig`

- Show the parameters and statistics of a specific interface:

`iwconfig {{interface}}`

- Set the ESSID (network name) of an specific interface (e.g., eth0 or wlp2s0):

`iwconfig {{interface}} {{new_network_name}}`

- Set the operating mode of an specific interface:

`ifconfig {{interface}} mode {{ad hoc|Managed|Master|Repeater|Secondary|Monitor|Auto}}`
