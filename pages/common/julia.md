# julia

> A high-level, high-performance dynamic programming language for technical computing.
> More information: <https://docs.julialang.org/en/v1/manual/getting-started/>.

- Start a REPL (interactive shell):

`julia`

- Execute a Julia program and exit:

`julia {{program.jl}}`

- Execute a Julia program that takes arguments:

`julia {{program.jl}} {{arguments}}`

- Evaluate a string containing Julia code:

`julia -e '{{julia_code}}'`

- Evaluate a string of Julia code, passing arguments to it:

`julia -e '{{for x in ARGS; println(x); end}}' {{arguments}}`

- Evaluate an expression and print the result:

`julia -E '{{(1 - cos(pi/4))/2}}'`

- Start Julia in parallel mode, using N worker processes:

`julia -p {{N}}`
