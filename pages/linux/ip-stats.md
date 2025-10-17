# ip stats

> Manage and show interface statistics.
> More information: <https://manned.org/ip-stats>.

- Show all interface statistics across all network devices:

`ip {{[st|stats]}} show`

- Show statistics for a specific network interface:

`ip {{[st|stats]}} show dev {{network_interface}}`

- Show link-layer statistics (same as `ip -s link show`):

`ip {{[st|stats]}} show group link`

- Show hardware offload statistics for all devices:

`ip {{[st|stats]}} show group offload`

- Show offload statistics for a specific interface:

`ip {{[st|stats]}} show dev {{network_interface}} group offload`

- Show a specific offload subgroup:

`ip {{[st|stats]}} show dev {{network_interface}} group offload subgroup {{l3_stats|cpu_hit|hw_stats_info}}`

- Show address-family specific statistics (e.g. MPLS):

`ip {{[st|stats]}} show group afstats subgroup {{mpls}}`

- Enable Layer 3 hardware statistics collection on a device:

`ip {{[st|stats]}} set dev {{network_interface}} l3_stats on`
