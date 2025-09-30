# act

> Voer GitHub-acties lokaal uit met behulp van Docker.
> Meer informatie: <https://manned.org/act>.

- Maak een lijst van de beschikbare acties:

`act {{[-l|--list]}}`

- Voer de standaard evenement uit:

`act`

- Voer een specifiek evenement uit:

`act {{evenement_type}}`

- Voer een specifieke job uit:

`act {{[-j|--job]}} {{job_id}}`

- Voer de acties [n]iet daadwerkelijk uit (d.w.z. een dry-run):

`act {{[-n|--dryrun]}}`

- Toon uitgebreide logboeken:

`act {{[-v|--verbose]}}`

- Voer een specifieke workflow uit:

`act push {{[-W|--workflows]}} {{pad/naar/workflow}}`
