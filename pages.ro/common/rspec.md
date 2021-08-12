# rspec

> Cadrul de testare de dezvoltare bazat pe comportament scris în Ruby pentru a testa codul Ruby.
> Mai multe informaţii: <https://rspec.info>

- Inițializează o configurație .rspec și un fișier de ajutor spec:

`rspec --init`

- Rulați toate testele:

`rspec`

- Rulați un anumit director de teste:

`rspec {{path/to/directory}}`

- Rulați un anumit fișier de testare:

`rspec {{path/to/file}}`

- Rulați mai multe fișiere de testare:

`rspec {{path/to/file1}} {{path/to/file2}}`

- Rulați un test specific într-un fișier (de exemplu, testul începe pe linia 83):

`rspec {{path/to/file}}:{{83}}`

- Rulați specificații cu o anumită sămânță:

`rspec --seed {{seed_number}}`
