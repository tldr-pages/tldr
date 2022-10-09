# sysbench

> Benchmark a System's CPU, IO and memory.
> More information: <https://github.com/akopytov/sysbench/>.

- Run a CPU benchmark with 1 thread for 10 seconds:

`sysbench cpu run`

- Run a CPU benchmark with multiple threads for a specified time:

`sysbench --threads={{number_of_threads}} --time={{seconds}}`

- Run a memory benchmark with 1 thread for 10 seconds:

`sysbench memory run`

- Prepare a filesystem-level read benchmark:

`sysbench fileio prepare`

- Run a filesystem-level benchmark:

`sysbench --file-test-mode={{rndrd|rndrw|rndwr|seqrd|seqrewr|seqwr}} fileio run`
