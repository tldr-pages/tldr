# bc

> Linguaggio per calcolatrice a precisione arbitraria.
> Vedi anche: `dc`, `qalc`.
> Maggiori informazioni: <https://manned.org/bc>.

- Avvia una sessione interattiva:

`bc`

- Avvia una sessione interattiva con la libreria matematica standard abilitata:

`bc {{[-i|--interactive]}} {{[-l|--mathlib]}}`

- Calcola un'espressione:

`echo '{{5 / 3}}' | bc`

- Esegue uno script:

`bc {{percorso/allo/script.bc}}`

- Calcola un'espressione con la scala specificata:

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- Calcola funzioni seno/coseno/arcotangente/logaritmo_naturale/esponenziale con `mathlib`:

`echo '{{s|c|a|l|e}}({{1}})' | bc {{[-l|--mathlib]}}`

- Esegue uno script fattoriale inline:

`echo "define factorial(n) { if (n <= 1) return 1; return n*factorial(n-1); }; factorial({{10}})" | bc`
