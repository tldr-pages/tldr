# sh5util

> Merge HDF5 files produced by the `sacct_gather_profile` plugin.
> More information: <https://slurm.schedmd.com/sh5util.html>.

- Merge HDF5 files produced on each allocated node for the specified job or step:

`sh5util --jobs={{job_id|job_id.step_id}}`

- Extract one or more data series from a merged job file:

`sh5util --jobs={{job_id|job_id.step_id}} --extract -i {{path/to/file.h5}} --series={{Energy|Filesystem|Network|Task}}`

- Extract one data item from all nodes in a merged job file:

`sh5util --jobs={{job_id|job_id.step_id}} --item-extract --series={{Energy|Filesystem|Network|Task}} --data={{data_item}}`
