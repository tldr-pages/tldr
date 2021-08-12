# convmv

> Conversia numelor de fișiere (NU conținut de fișier) de la o codificare la alta.
> Mai multe informaţii: <https://www.j3e.de/linux/convmv/man/>

- Testați conversia codificării numelui fișierului (nu schimbați de fapt numele fișierului):

`convmv -f {{from_encoding}} -t {{to_encoding}} {{input_file}}`

- Convertiți codificarea numelui de fișier și redenumiți fișierul la noua codificare:

`convmv -f {{from_encoding}} -t {{to_encoding}} --notest {{input_file}}`
