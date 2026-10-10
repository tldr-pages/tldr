# jj workspace

> Beheer Jujutsu-werkruimtes.
> Meer informatie: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-workspace>.

- Toon alle werkruimtes die aan de repository gekoppeld zijn:

`jj workspace list`

- Maak een nieuwe werkruimte aan op het opgegeven pad:

`jj workspace add {{pad/naar/map}}`

- Maak een nieuwe werkruimte aan met een specifieke naam en bovenliggende revisie:

`jj workspace add --name {{werkruimte_naam}} {{[-r|--revision]}} {{revisie}} {{pad/naar/map}}`

- Toon de hoofdmap van de huidige werkruimte:

`jj workspace root`

- Toon de hoofdmap van een specifieke werkruimte:

`jj workspace root --name {{werkruimte_naam}}`

- Hernoem de huidige werkruimte:

`jj workspace rename {{nieuwe_naam}}`

- Stop met het volgen van een werkruimte zonder de bestanden te verwijderen:

`jj workspace forget {{werkruimte_naam}}`

- Werk een werkruimte bij waarvan de werkkopie verouderd is:

`jj workspace update-stale`
