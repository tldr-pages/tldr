# fold

> Breek lange regels af voor uitvoerapparaten met vaste breedte.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/fold-invocation.html>.

- Breek regels af met een vaste breedte:

`fold --width {{breedte}} {{pad/naar/bestand}}`

- Tel breedte in bytes (standaard is het tellen in kolommen):

`fold --bytes --width {{breedte_in_bytes}} {{pad/naar/bestand}}`

- Breek de regel na de meest rechtse spatie binnen de breedtelimiet:

`fold --spaces --width {{breedte}} {{pad/naar/bestand}}`
