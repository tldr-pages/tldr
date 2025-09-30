# cdecl

> Compose and decode C and C++ type declarations.
> More information: <https://manned.org/cdecl>.

- Compose English phrase into C declaration, and create [c]ompilable output (include `;` and `{}`):

`cdecl -c {{phrase}}`

- Explain C declaration in English:

`cdecl explain {{C_declaration}}`

- Cast a variable to another type:

`cdecl cast {{variable_name}} to {{type}}`

- Run in [i]nteractive mode:

`cdecl -i`
