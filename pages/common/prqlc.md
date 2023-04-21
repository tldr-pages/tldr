# prqlc

> PRQL compiler.
> PRQL is a modern language for transforming data - a simple, powerful, pipelined SQL replacement.
> More information: <https://prql-lang.org>.

- Run the compiler interactively:

`prqlc compile`

- Compile a specific `.prql` file to stdout:

`prqlc compile {{path/to/file.prql}}`

- Compile a `.prql` file to a `.sql` file:

`prqlc compile {{path/to/source.prql}} {{path/to/target.sql}}`

- Compile a query:

`echo "{{from employees | filter has_dog | select salary}}" | prqlc compile`

- Watch a directory and compile on file modification:

`prqlc watch {{path/to/directory}}`
