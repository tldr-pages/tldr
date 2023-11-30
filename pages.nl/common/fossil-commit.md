# fossil commit

> Commit bestanden naar een Fossil repository.
> Meer informatie: <https://fossil-scm.org/home/help/commit>.

- Maak een nieuwe versie met alle aanpassingen in de huidige checkout; de gebruiker zal gevraagd worden voor een opmerking:

`fossil commit`

- Maak een nieuwe versie met alle aanpassingen in de huidige checkout en maak gebruik van de gespecificeerde opmerking:

`fossil commit --comment "{{opmerking}}"`

- Maak een nieuwe versie met alle aanpassingen in de huidige checkout met een comment ingelezen vanaf een specifiek bestand:

`fossil commit --message-file {{pad/naar/commit_message_bestand}}`

- Maak een nieuwe versie met aanpassingen van de gespecificeerde bestanden; de gebruiker zal gevraagd worden voor een opmerking:

`fossil commit {{pad/naar/bestand1}} {{pad/naar/bestand2}}`
