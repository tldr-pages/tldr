# hyperfine

> Strumento di benchmarking con interfaccia CLI.
> Maggiori informazioni: <https://github.com/sharkdp/hyperfine/>.

- Esegui un benchmark di base, eseguendo almeno 10 esecuzioni:

`hyperfine '{{make}}'`

- Esegui un benchmark comparativo:

`hyperfine '{{make target1}}' '{{make target2}}'`

- Modifica il numero minimo di esecuzioni di benchmark:

`hyperfine --min-runs {{7}} '{{make}}'`

- Esegui benchmark con periodo di riscaldamento:

`hyperfine --warmup {{5}} '{{make}}'`

- Esegui un comando prima di ogni esecuzione di benchmark (per cancellare le cache, etc.):

`hyperfine --prepare '{{make clean}}' '{{make}}'`

- Esegui un benchmark in cui un singolo parametro cambia per ogni esecuzione:

`hyperfine --prepare '{{make clean}}' --parameter-scan {{num_threads}} {{1}} {{10}} '{{make -j {num_threads}}}'`
