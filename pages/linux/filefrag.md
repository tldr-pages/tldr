# filefrag

> Report how badly fragmented a particular file might be.
> More information: <https://linux.die.net/man/8/filefrag>.

- Report on file fragmentation:

`filefrag {{file}}`

- Generate report for multiple files:

`filefrag {{file1}} {{file2}}`

- Use 1024 byte blocksize for the output:

`filefrag -b {{files}}`

- Sync the file before requesting the mapping:

`filefrag -s {{files}}`

- Display mapping of extended attributes:

`filefrag -x {{files}}`

- Be verbose when checking for file fragmentation:

`filefrag -v {{files}}`
