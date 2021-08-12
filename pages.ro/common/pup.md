# pup

> Instrument de analiză HTML în linie de comandă.
> Mai multe informaţii: <https://github.com/ericchiang/pup>

- Transformați un fișier HTML brut într-un format curățat, indentat și colorat:

`cat {{index.html}} | pup --color`

- Filtrare HTML după numele etichetei element:

`cat {{index.html}} | pup '{{tag}}'`

- Filtrează HTML după id:

`cat {{index.html}} | pup '{{div#id}}'`

- Filtru HTML după valoarea atributului

`cat {{index.html}} | pup '{{input[type="text"]}}'`

- Imprimați tot textul din elementele HTML filtrate și copiii lor:

`cat {{index.html}} | pup '{{div}} text{}'`

- Imprimare HTML ca JSON:

`cat {{index.html}} | pup '{{div}} json{}'`
