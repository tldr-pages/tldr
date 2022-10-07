# sysbench

> Benchmark your System's cpu, io and memory. 
> More information : <https://github.com/akopytov/sysbench> 

- Run a cpu benchmark with 1 thread for 10 seconds:

`sysbench cpu run`

- Run a cpu benchmark with multiple threads for a specified time:

`sysbench --threads={{number_of_threads}} --time={{seconds}}`

- Run a memory benchmark with 1 thread for 10 seconds

`sysbench memory run`

- Prepare a fileio read benchmark:

`sysbench fileio prepare`

- Run a fileio benchmark {seqwr, seqrewr, seqrd, rndrd, rndwr, rndrw}:

`sysbench --file-test-mode={{test_mode}} fileio run`