# phploc

> Un instrument pentru măsurarea rapidă a dimensiunii și analizarea structurii unui proiect PHP.
> Mai multe informaţii: <https://github.com/sebastianbergmann/phploc>

- Analizați un director și imprimați rezultatul:

`phploc {{path/to/directory}}`

- Includeți numai fișiere specifice dintr-o listă separată prin virgulă (globuri sunt permise):

`phploc {{path/to/directory}} --names {{files}}`

- Excludeți anumite fișiere dintr-o listă separată prin virgulă (globuri sunt permise):

`phploc {{path/to/directory}} --names-exclude {{files}}`

- Excludeți un anumit director din analiză:

`phploc {{path/to/directory}} --exclude {{path/to/exclude_directory}}`

- Conectaţi rezultatele la un anumit fişier CSV:

`phploc {{path/to/directory}} --log-csv {{path/to/file}}`

- Conectaţi rezultatele la un anumit fişier XML:

`phploc {{path/to/directory}} --log-xml {{path/to/file}}`

- Numărarea claselor de cazuri de testare phpunIT și metode de testare:

`phploc {{path/to/directory}} --count-tests`
