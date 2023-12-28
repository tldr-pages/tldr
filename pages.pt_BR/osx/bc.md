# bc

> Linguagem e calculadora com precisão arbitrária.
> Veja também: `dc`.
> Mais informações: <https://manned.org/man/freebsd-13.0/bc.1>.

- Inicia uma sessão interativa:

`bc`

- Inicia uma sessão interativa com a biblioteca matemática padrão habilitada:

`bc --mathlib`

- Calcula uma expressão:

`bc --expression='{{5 / 3}}'`

- Executa um script:

`bc {{caminho/para/script.bc}}`

- Calcula uma expressão com a escala especificada:

`bc --expression='scale = {{10}}; {{5 / 3}}'`

- Calcula uma função sine/cosine/arctangent/natural logarithm/exponential usando `mathlib`:

`bc --mathlib --expression='{{s|c|a|l|e}}({{1}})'`
