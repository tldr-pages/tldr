# sh5util

> Tool for merging HDF5 files from the acct_gather_profile plugin that gathers detailed data for jobs running under `Slurm`.
> More information: <https://manned.org/sh5util>.

- Extract all data from specific nodes:

`sh5util --jobs={{job1.step1,job2.step2,...}} --node={{string}} --level={{Node:Totals|Node:TimeSeries}} --series={{Energy|Filesystem|Network|Task|Task_id}}`
