# acyclic

> Construit un graphe orienté acyclique en inversant quelques sommets.
> Filtres Graphviz : `acyclic`, `bcomps`, `comps`, `edgepaint`, `gvcolor`, `gvpack`, `mingle`, `nop`, `sccmap`, `tred`, & `unflatten`.
> Plus d'informations : <https://graphviz.org/pdf/acyclic.1.pdf>.

- Construit un graphe orienté acyclique en inversant quelques sommets :

`acyclic {{chemin/vers/entrée.gv}} > {{chemin/vers/sortie.gv}}`

- Affiche si un graphe est acyclique, possède une boucle ou est non-dirigé, ne produit pas de graphe en sortie :

`acyclic -v -n {{chemin/vers/entrée.gv}}`

- Affiche l'aide d' `acyclic` :

`acyclic -?`
