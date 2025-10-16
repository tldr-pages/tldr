# ip stats

> Manage and show interface statistics.
> Part of the `iproute2` suite.
> More information: <https://man7.org/linux/man-pages/man8/ip-stats.8.html>.
- Show all interface statistics across all network devices:

`ip stats show`

- Show statistics for a specific network interface:

`ip stats show dev {{network_interface}}`

- Show link-layer statistics (same as `ip -s link show`):

`ip stats show group link`

- Show hardware offload statistics for all devices:

`ip stats show group offload`

- Show offload statistics for a specific interface:

`ip stats show dev {{network_interface}} group offload`

- Show a specific offload subgroup, such as `l3_stats`:

`ip stats show dev {{network_interface}} group offload subgroup {{l3_stats|cpu_hit|hw_stats_info}}`

- Show address-family specific statistics (e.g. MPLS):

`ip stats show group afstats subgroup {{mpls}}`

- Enable Layer 3 hardware statistics collection on a device:

`ip stats set dev {{network_interface}} l3_stats on`

- Disable Layer 3 hardware statistics collection on a device:

`ip stats set dev {{network_interface}} l3_stats off`

- Show extended statistics for bridge or bond devices:

`ip stats show group xstats subgroup {{bridge|bond}}`

- Show extended statistics for bridge slaves:

`ip stats show group xstats_slave subgroup bridge`
