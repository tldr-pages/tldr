# ag

> Căutătorul de argint. Ca și ACK, dar își propune să fie mai rapid.
> Mai multe informaţii: <https://github.com/ggreer/the_silver_searcher>

- Găsiți fișiere care conțin „foo” și imprimați potrivirile liniei în context:

`ag {{foo}}`

- Găsiți fișiere care conțin „foo” într-un anumit director:

`ag {{foo}} {{path/to/directory}}`

- Găsiți fișiere care conțin „foo”, dar listați numai numele fișierelor:

`ag -l {{foo}}`

- Găsiți fișiere care conțin „FOO” caz insensibil, și imprimați numai meciul, mai degrabă decât întreaga linie:

`ag -i -o {{FOO}}`

- Găsiți „foo” în fișiere cu un nume care se potrivește „bar”:

`ag {{foo}} -G {{bar}}`

- Găsiți fișiere al căror conținut se potrivește cu o expresie regulată:

`ag '{{^ba(r|z)$}}'`

- Găsiți fișiere cu un nume care se potrivește „foo”:

`ag -g {{foo}}`
