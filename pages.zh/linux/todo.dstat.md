# dstat

> Versatile tool for generating system resource statistics.
> More information: <http://dag.wieers.com/home-made/dstat>.

- Display CPU, disk, net, paging and system statistics:

`dstat`

- Display statistics every 5 seconds and 4 updates only:

`dstat {{5}} {{4}}`

- Display CPU and memory statistics only:

`dstat --cpu --mem`

- List all available dstat plugins:

`dstat --list`

- Display the process using the most memory and most CPU:

`dstat --top-mem --top-cpu`

- Display battery percentage and remaining battery time:

`dstat --battery --battery-remain`
