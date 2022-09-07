# lualatex

> An extended version of TeX using Lua to compile.
> More information: <https://manned.org/lualatex.1>.

- Start `texlua` to act as a Lua interpreter:

`lualatex`

- Compile a Tex file to PDF:

`lualatex {{path/to/file.tex}}`

- Compile a Tex file without error interruption:

`lualatex -interaction nonstopmode {{path/to/file.tex}}`

- Compile a Tex file with a specific output file name:

`lualatex -jobname={{filename}} {{path/to/file.tex}}`
