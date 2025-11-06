# hwloc

> Manage and query hardware topology information.
> Part of the Portable Hardware Locality (hwloc) toolset.
> More information: <https://manned.org/hwloc>.

- Display the machine topology in a tree format:

`hwloc-ls`

- Show a compact listing of available CPUs:

`hwloc-ls --cpus`

- Display only physical cores (ignore logical processors):

`hwloc-ls --only pu`

- Export topology to an XML file:

`hwloc-ls --output-format xml --output-file {{path/to/topology.xml}}`

- Show the topology of a specific process:

`hwloc-ls --pid {{pid}}`

- Display I/O devices in the topology:

`hwloc-ls --io`

- Show memory hierarchy information:

`hwloc-ls --memory`

- Display the topology with physical indexes:

`hwloc-ls --physical`
