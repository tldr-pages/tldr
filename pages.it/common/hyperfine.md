# hyperfine

> Strumento di benchmarking con interfaccia CLI.
> Maggiori informazioni: <https://manned.org/hyperfine>.

- Esegui un benchmark di base, eseguendo almeno 10 esecuzioni:

`hyperfine '{{make}}'`

- Esegui un benchmark comparativo:

`hyperfine '{{make target1}}' '{{make target2}}'`

- Modifica il numero minimo di esecuzioni di benchmark:

`hyperfine {{[-m|--min-runs]}} {{7}} '{{make}}'`

- Esegui benchmark con periodo di riscaldamento:

`hyperfine {{[-w|--warmup]}} {{5}} '{{make}}'`

- Esegui un comando prima di ogni esecuzione di benchmark (per cancellare le cache, etc.):

`hyperfine {{[-p|--prepare]}} '{{make clean}}' '{{make}}'`

- Esegui un benchmark in cui un singolo parametro cambia per ogni esecuzione:

`hyperfine {{[-p|--prepare]}} '{{make clean}}' {{[-P|--parameter-scan]}} {{num_threads}} {{1}} {{10}} '{{make --jobs {num_threads}}}'`
