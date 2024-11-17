# bc

> Uma linguagem de calculadora de precisão arbitrária.
> Veja também: `dc`, `qalc`.
> Mais informações: <https://manned.org/bc>.

- Inicia uma sessão interativa:

`bc`

- Inicia uma sessão [i]nterativa com a biblioteca padrão habilitada:

`bc --interactive --mathlib`

- Calcula uma expressão:

`echo '{{5 / 3}}' | bc`

- Executa um script:

`bc {{caminho/para/script.bc}}`

- Calcula uma expressão com a escala especificada:

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- Calcula uma função seno/cosseno/arco tangente/logaritmo natural/função exponencial usando `mathlib`:

`echo '{{s|c|a|l|e}}({{1}})' | bc --mathlib`

- Executa um script fatorial a partir da linha de comando:

`echo "define factorial(n) { if (n <= 1) return 1; return n*factorial(n-1); }; factorial({{10}})" | bc`
