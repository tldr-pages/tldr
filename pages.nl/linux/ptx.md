# ptx

> Genereer een permutatie-index van woorden uit tekstbestanden.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/ptx-invocation.html>.

- Genereer een permutatie-index waarbij het eerste veld van elke regel een indexreferentie is:

`ptx {{[-r|--references]}} {{pad/naar/bestand}}`

- Genereer een permutatie-index met automatisch gegenereerde indexreferenties:

`ptx {{[-A|--auto-reference]}} {{pad/naar/bestand}}`

- Genereer een permutatie-index met een vaste breedte:

`ptx {{[-w|--width]}} {{breedte_in_kolommen}} {{pad/naar/bestand}}`

- Genereer een permutatie-index met een lijst van gefilterde woorden:

`ptx {{[-o|--only-file]}} {{pad/naar/filter}} {{pad/naar/bestand}}`

- Genereer een permutatie-index met SYSV-stijl gedragingen:

`ptx {{[-G|--traditional]}} {{pad/naar/bestand}}`
