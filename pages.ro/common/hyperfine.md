# hyperfine

> Un instrument de analiză comparativă în linia de comandă.
> Mai multe informaţii: <https://github.com/sharkdp/hyperfine/>

- Rulați un criteriu de referință de bază, efectuând cel puțin 10 curse:

`hyperfine '{{make}}'`

- Rulați o referință comparativă:

`hyperfine '{{make target1}}' '{{make target2}}'`

- Modificarea numărului minim de runde de benchmarking:

`hyperfine --min-runs {{7}} '{{make}}'`

- Efectuați un criteriu de referință cu încălzire:

`hyperfine --warmup {{5}} '{{make}}'`

- Rulați o comandă înainte de fiecare rulare de referință (pentru a șterge cache-uri, etc.):

`hyperfine --prepare '{{make clean}}' '{{make}}'`

- Rulați un criteriu de referință în cazul în care un singur parametru se modifică pentru fiecare rulare:

`hyperfine --prepare '{{make clean}}' --parameter-scan {{num_threads}} {{1}} {{10}} '{{make -j {num_threads}}}'`
