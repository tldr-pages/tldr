# ptx

> Genereer een permutatie-index van woorden uit tekstbestanden.
> Meer informatie: <https://www.gnu.org/software/coreutils/ptx>.

- Genereer een permutatie-index waarbij het eerste veld van elke regel een indexreferentie is:

`ptx --references {{pad/naar/bestand}}`

- Genereer een permutatie-index met automatisch gegenereerde indexreferenties:

`ptx --auto-reference {{pad/naar/bestand}}`

- Genereer een permutatie-index met een vaste breedte:

`ptx --width={{breedte_in_kolommen}} {{pad/naar/bestand}}`

- Genereer een permutatie-index met een lijst van gefilterde woorden:

`ptx --only-file={{pad/naar/filter}} {{pad/naar/bestand}}`

- Genereer een permutatie-index met SYSV-stijl gedragingen:

`ptx --traditional {{pad/naar/bestand}}`
