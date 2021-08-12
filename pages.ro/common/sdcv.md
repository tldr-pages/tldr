# sdcv

> StarDdict, un client de dicționar de linie de comandă.
> Dicționarele sunt furnizate separat de client.
> Mai multe informaţii: <https://manned.org/sdcv>

- Începeți sdcv interactiv:

`sdcv`

- Lista dicționarelor instalate:

`sdcv --list-dicts`

- Afișează o definiție dintr-un anumit dicționar:

`sdcv --use-dict {{dictionary_name}} {{search_term}}`

- Caută o definiție cu o căutare neclară:

`sdcv {{search_term}}`

- Caută o definiție cu o căutare exactă:

`sdcv --exact-search {{search_term}}`

- Caută o definiție și formatează ieșirea ca JSON:

`sdcv --json {{search_term}}`

- Căutați dicționare într-un anumit director:

`sdvc --data-dir {{path/to/directory}} {{search_term}}`
