# btm

> Display system information about the CPU, memory, disks, network and processes.
> An enhanced alternative to `top`.
> See also: `btop`, `glances`, `atop`, `htop`, `top`.
> More information: <https://clementtsang.github.io/bottom/nightly/#usage-and-configuration>.

- Show the default layout (CPU, memory, temperatures, disk, network, and processes):

`btm`

- Enable basic mode, removing charts and condensing data (similar to `top`):

`btm {{[-b|--basic]}}`

- Use big dots instead of small ones in charts:

`btm {{[-m|--dot_marker]}}`

- Show also battery charge and health status:

`btm --battery`

- Refresh every 250 milliseconds and show the last 30 seconds in the charts:

`btm {{[-r|--rate]}} 250 {{[-t|--default_time_value]}} 30000`
