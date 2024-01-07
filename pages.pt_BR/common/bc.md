# bc

> Uma linguagem de calculadora de precisão arbitrária.
> Veja também: `dc`.
> Mais informações: <https://manned.org/man/bc.1>.

- Inicia uma sessão interativa:

`bc`

- Inicia uma sessão interativa com a biblioteca matemática padrão ativada:

`bc --mathlib`

- Calcula uma expressão:

`echo '{{5 / 3}}' | bc`

- Executa um script:

`bc {{caminho/para/script.bc}}`

- Calcula uma expressão com a escala especificada:

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- Calcula uma função seno/cosseno/arco tangente/logaritmo natural/função exponencial usando `mathlib`:

`echo '{{s|c|a|l|e}}({{1}})' | bc --mathlib`
