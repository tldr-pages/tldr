# conan

> Managerul de pachete open source, descentralizat și cross-platform pentru a crea și partaja toate fișierele binare native.
> Mai multe informaţii: <https://conan.io/>

- Instalați pachete bazate pe `conanfile.txt`:

`conan install {{.}}`

- Instalați pachete și creați fișiere de configurare pentru un anumit generator:

`conan install -g {{generator}}`

- Instalați pachete, construind din sursă:

`conan install {{.}} --build`

- Caută pachete instalate local:

`conan search {{package}}`

- Căutați pachete la distanță:

`conan search {{package}} -r {{remote}}`

- Lista telecomenelor:

`conan remote list`
