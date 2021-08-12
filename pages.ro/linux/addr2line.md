# addr2line

> Conversia adreselor unui binar în nume de fișiere și numere de linie.
> Mai multe informaţii: <https://manned.org/addr2line>

- Afișați numele fișierului și numărul de linie al codului sursă de la o adresă de instrucțiuni a unui executabil:

`addr2line --exe={{path/to/executable}} {{address}}`

- Afișează numele funcției, numele fișierului și numărul liniei:

`addr2line --exe={{path/to/executable}} --functions {{address}}`

- Solicită numele funcției pentru codul C++:

`addr2line --exe={{path/to/executable}} --functions --demangle {{address}}`
