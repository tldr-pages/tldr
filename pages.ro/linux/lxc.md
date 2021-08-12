# lxc

> Gestionați containerele Linux utilizând API-ul Lxd REST.
> Orice nume de containere sau modele pot fi prefixate cu numele unui server la distanță.

- Listează containerele locale care corespund unui șir. Omiteți șirul pentru a lista toate containerele locale:

`lxc list {{match_string}}`

- Lista de imagini care se potrivesc unui șir. Omiteți șirul pentru a lista toate imaginile:

`lxc image list [{{remote}}:]{{match_string}}`

- Creați un nou container dintr-o imagine:

`lxc init [{{remote}}:]{{image}} {{container}}`

- Porniți un container:

`lxc start [{{remote}}:]{{container}}`

- Opreşte un container:

`lxc stop [{{remote}}:]{{container}}`

- Arată informații detaliate despre un container:

`lxc info [{{remote}}:]{{container}}`

- Luați un instantaneu al unui container:

`lxc snapshot [{{remote}}:]{{container}} {{snapshot}}`
