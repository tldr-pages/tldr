# gox

> Un instrument pentru compilarea încrucișată a programelor Go.
> Mai multe informaţii: <https://github.com/mitchellh/gox>

- Compilare Go program în directorul curent pentru toate sistemele de operare și combinațiile de arhitectură:

`gox`

- Descărcați și compilați un program Go de la un URL la distanță:

`gox {{url_1}} {{url_2}}`

- Compilați directorul curent pentru un anumit sistem de operare:

`gox -os="{{os}}"`

- Compilați directorul curent pentru o singură combinație de sistem de operare și arhitectură:

`gox -osarch="{{os}}/{{arch}}"`
