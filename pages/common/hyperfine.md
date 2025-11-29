# hyperfine

> A benchmarking tool.
> More information: <https://manned.org/hyperfine>.

- Run a basic benchmark, performing at least 10 runs:

`hyperfine '{{make}}'`

- Run a comparative benchmark:

`hyperfine '{{make target1}}' '{{make target2}}'`

- Change minimum number of benchmarking runs:

`hyperfine {{[-m|--min-runs]}} {{7}} '{{make}}'`

- Perform benchmark with warmup:

`hyperfine {{[-w|--warmup]}} {{5}} '{{make}}'`

- Run a command before each benchmark run (to clear caches, etc.):

`hyperfine {{[-p|--prepare]}} '{{make clean}}' '{{make}}'`

- Run a benchmark where a single parameter changes for each run:

`hyperfine {{[-p|--prepare]}} '{{make clean}}' {{[-P|--parameter-scan]}} {{num_threads}} {{1}} {{10}} '{{make --jobs {num_threads}}}'`
