# lualatex

> An extended version of TeX using Lua to compile.
> More information: <https://manned.org/lualatex.1>.

- Start `texlua` to act as Lua interpreter:

`lualatex`

- Compile Tex file to PDF:

`lualatex {{path/to/file.tex}}`

- Compile Tex file without error interruption:

`lualatex -interaction nonstopmode {{path/to/file.tex}}`

- Compile Tex file with a specific output file name:

`lualatex -jobname={{filename}} {{path/to/file.tex}}`
