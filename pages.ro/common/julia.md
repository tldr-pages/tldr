# julia

> Un limbaj de programare dinamic la nivel înalt, de înaltă performanță, pentru calcul tehnic.
> Mai multe informaţii: <https://docs.julialang.org/en/v1/manual/getting-started/>

- Începe o sesiune Julia REPL:

`julia`

- Executați un program Julia și ieșiți:

`julia {{program.jl}}`

- Executa un program Julia care ia argumente:

`julia {{program.jl}} {{arguments}}`

- Evaluați un șir care conține codul Julia:

`julia -e '{{julia_code}}'`

- Evaluați un șir de cod Julia, trecând argumente la ea:

`julia -e '{{for x in ARGS; println(x); end}}' {{arguments}}`

- Evaluați o expresie și imprimați rezultatul:

`julia -E '{{(1 - cos(pi/4))/2}}'`

- Porniți Julia în modul paralel, folosind procesele de lucru N:

`julia -p {{N}}`
