# pushd

> Plaats een map op een stack zodat deze later kan worden benaderd.
> Zie ook: `popd` om terug te schakelen naar de originele map en `dirs` om de inhoud van de mapstapel weer te geven.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-pushd>.

- Schakel naar een map en zet deze op de stapel:

`pushd {{pad/naar/map}}`

- Wissel de eerste en tweede mappen op de stapel:

`pushd`

- Draai de stapel door het 5e element bovenaan te plaatsen:

`pushd +4`

- Draai de stapel 4 keer naar links (de huidige map blijft bovenaan door het 5e element te vervangen):

`pushd -n +4`
