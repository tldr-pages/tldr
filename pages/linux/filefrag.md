# filefrag

> Report how badly fragmented a particular file might be.
> More information: <https://manned.org/filefrag>.

- Display a report for one or more files:

`filefrag {{path/to/file1 path/to/file2 ...}}`

- Display a report using a 1024 byte blocksize:

`filefrag -b {{path/to/file}}`

- Sync the file before requesting the mapping:

`filefrag -s {{path/to/file1 path/to/file2 ...}}`

- Display mapping of extended attributes:

`filefrag -x {{path/to/file1 path/to/file2 ...}}`

- Display a report with verbose information:

`filefrag -v {{path/to/file1 path/to/file2 ...}}`
