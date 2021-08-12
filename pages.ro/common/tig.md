# tig

> O interfață în mod text pentru Git.
> Mai multe informaţii: <https://github.com/jonas/tig>

- Afișați secvența de angajări pornind de la cea curentă în ordine cronologică inversă:

`tig`

- Afișați istoria unei ramuri specifice:

`tig {{branch}}`

- Afișați istoricul anumitor fișiere sau directoare:

`tig {{path1 path2 …}}`

- Afișați diferența dintre două referințe (cum ar fi ramuri sau etichete):

`tig {{base_ref}}..{{compared_ref}}`

- Afișarea se angajează din toate ramurile și stashes:

`tig --all`

- Începeți în vizualizarea stash, afișând toate stash-urile salvate:

`tig stash`
