# gdc

> D compiler using GCC as a backend.
> More information: <https://wiki.dlang.org/Using_GDC>.

- Create an executable:

`gdc {{path/to/source.d}} -o {{path/to/output_executable}}`

- Print information about module dependencies:

`gdc -fdeps`

- Generate Ddoc documentation:

`gdc -fdoc`

- Generate D interface files:

`gdc -fintfc`

- Do not link the standard GCC libraries in the compilation:

`gdc -nostdlib`
