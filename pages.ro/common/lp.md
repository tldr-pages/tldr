# lp

> Imprimați fișiere.

- Tipăriți ieșirea unei comenzi la imprimanta implicită (vedeți comanda `lpstat):

`echo "test" | lp`

- Imprimați un fișier la imprimanta implicită:

`lp {{path/to/filename}}`

- Imprimați un fișier la o imprimantă denumită (a se vedea comanda `lpstat`):

`lp -d {{printer_name}} {{path/to/filename}}`

- Imprimați N copii ale fișierului la imprimanta implicită (înlocuiți N cu numărul dorit de copii):

`lp -n {{N}} {{path/to/filename}}`

- Imprimați numai anumite pagini la imprimanta implicită (imprimați paginile 1, 3-5 și 16):

`lp -P 1,3-5,16 {{path/to/filename}}`

- Reluați imprimarea unei slujbe:

`lp -i {{job_id}} -H resume`
