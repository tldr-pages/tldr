# ltrace

> Afișați apelurile bibliotecii dinamice ale unui proces.
> Mai multe informaţii: <https://manned.org/ltrace>

- Imprimare (urmărire) apeluri de bibliotecă ale unui program binar:

`ltrace ./{{program}}`

- Contele apeluri de la bibliotecă. Imprimați un rezumat la îndemână în partea de jos:

`ltrace -c {{path/to/program}}`

- Trace apeluri la malloc și gratuit, omite cele făcute de libc:

`ltrace -e malloc+free-@libc.so* {{path/to/program}}`

- Scrie în fișier în loc de terminal:

`ltrace -o {{file}} {{path/to/program}}`
