# whatis

> Afișează descrieri dintr-o singură linie din paginile manuale.

- Afișează o descriere dintr-o pagină de om:

`whatis {{command}}`

- Nu tăia descrierea de la capătul liniei:

`whatis --long {{command}}`

- Afișează descrieri pentru toate comenzile care se potrivesc unui glob:

`whatis --wildcard {{net*}}`

- Căutare descrieri de pagini om cu o expresie regulată:

`whatis --regex '{{wish[0-9]\.[0-9]}}'`
