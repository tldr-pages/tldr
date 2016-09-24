# julia

> A high-level, high-performance dynamic programming language for technical computing.
> It aims to provide the ease-of-use of scripting languages with the speed of compiled languages.

- Start a Julia REPL session:

`julia`

- Execute a Julia program and exit:

`julia {{program.jl}}`

- Execute a Julia program that takes arguments:

`julia {{program.jl}} {{arguments}}`

- Evaluate a string containing Julia code:

`julia -e '{{julia_code}}'`

- Evaluate a string of Julia code, passing arguments to it:

`julia -e '{{for x in ARGS; println(x); end}}' {{arguments}}`

- Start Julia in parallel mode, using N worker processes:

`julia -p {{N}}`
