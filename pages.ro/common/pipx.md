# pipx

> Instalați și executați aplicații python în medii izolate.
> Mai multe informaţii: <https://github.com/pipxproject/pipx>

- Rulați o aplicație într-un mediu virtual temporar:

`pipx run {{pycowsay}} {{moo}}`

- Instalați un pachet într-un mediu virtual și adăugați puncte de intrare la cale:

`pipx install {{package}}`

- Lista pachetelor instalate:

`pipx list`

- Rulați o aplicație într-un mediu virtual temporar cu un nume de pachet diferit de executabil:

`pipx run --spec {{httpx-cli}} {{httpx}} {{http://www.github.com}}`
