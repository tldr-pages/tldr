# gdc

> GNU front-end D Compiler.
> More information: <https://wiki.dlang.org/Using_GDC>.

- Create an executable:

`gdc {{Source_Name}}.d -o {{Output_File_Name}}`

- Print information about module dependencies:

`gdc -fdeps`

- Generate Ddoc documentation:

`gdc -fdoc`

- Generate D interface files:

`gdc -fintfc`

- Do not link the standard gcc libraries in the compilation:

`gdc -nostdlib`
