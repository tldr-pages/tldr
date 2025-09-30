# git switch

> Passa ad altri rami. Richiede versioni di Git successive alla 2.23.
> Vedi anche `git checkout`.
> Maggiori informazioni: <https://git-scm.com/docs/git-switch>.

- Passa ad un altro ramo esistente:

`git switch {{nome_ramo}}`

- Crea un nuovo ramo e passa a quel ramo:

`git switch {{[-c|--create]}} {{nome_ramo}}`

- Crea un nuovo ramo a partire da un commit esistente e passa a quel ramo:

`git switch {{[-c|--create]}} {{nome_ramo}} {{commit}}`

- Torna al ramo precedente:

`git switch -`

- Passa ad un ramo ed aggiorna tutti i moduli secondari associati:

`git switch --recurse-submodules {{nome_ramo}}`

- Passa ad un ramo e uniscilo automaticamente al ramo corrente, include le modifiche non committate:

`git switch {{[-m|--merge]}} {{nome_ramo}}`
