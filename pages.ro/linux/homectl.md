# homectl

> Creați, eliminați, modificați sau inspectați directoarele de domiciliu utilizând serviciul de sistem.
> Mai multe informaţii: <https://man.archlinux.org/man/homectl.1>

- Listați conturile de utilizator și directoarele lor de acasă asociate:

`homectl list`

- Creați un cont de utilizator și directorul lor asociat:

`sudo homectl create {{username}}`

- Eliminați un anumit utilizator și directorul de acasă asociat:

`sudo homectl remove {{username}}`

- Schimbați parola pentru un anumit utilizator:

`sudo homectl passwd {{username}}`

- Rulați o coajă sau o comandă cu acces la un anumit director de acasă:

`sudo homectl with {{username}} -- {{command}} {{command_arguments}}`

- Blocați sau deblocați un anumit director de acasă:

`sudo homectl {{lock|unlock}} {{username}}`

- Schimbați spațiul pe disc atribuit unui anumit director de acasă la 100 GiB:

`sudo homectl resize {{username}} {{100G}}`

- Ajutor pentru afișare:

`homectl --help`
