# mbw

> Memory Bandwidth Benchmark.
> More information: <https://manned.org/mbw>.

- Run 3 memory bandwidth tests with 512MB size:

`mbw -n 3 512`

- Run 3 memory bandwidth tests with 512MB memory size, output only statistics, not averages:

`mbw -n 3 -q -a 512`

- Run memcpy test 3 times with 512MB size, only display statistics:

`mbw -n 3 -q -t{{0}} 512`

- Run the memcpy test 10 times with 1024 byte blocks allocated 8192MB of memory:

`mbw -n 10 -q -t{{2}} -b 1024 8192`

- Run dumb test with 2048MB size, output only statistics, run forever:

`mbw -n 0 -t{{1}} -q 2048`
