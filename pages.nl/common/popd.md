# popd

> Verwijder een map van de directory stack die is geplaatst met de ingebouwde pushd-opdracht van de shell.
> Zie ook: `pushd` om een map op de stapel te plaatsen en `dirs` om de inhoud van de stapel weer te geven.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-popd>.

- Verwijder de bovenste map van de stapel en ga ernaartoe:

`popd`

- Verwijder de N-de map (beginnend vanaf nul van links, uit de lijst die met `dirs` wordt weergegeven):

`popd +N`

- Verwijder de N-de map (beginnend vanaf nul van rechts, uit de lijst die met `dirs` wordt weergegeven):

`popd -N`

- Verwijder de eerste map (beginnend vanaf nul van links, uit de lijst die met `dirs` wordt weergegeven):

`popd -n`
