# act

> Voer GitHub-acties lokaal uit met behulp van Docker.
> Meer informatie: <https://github.com/nektos/act>.

- Maak een lijst van de beschikbare acties:

`act -l`

- Voer de standaard evenement uit:

`act`

- Voer een specifiek evenement uit:

`act {{evenement_type}}`

- Voer een specifieke actie uit:

`act -a {{actie_id}}`

- Voer de acties niet daadwerkelijk uit (d.w.z. een proefrit):

`act -n`

- Toon uitgebreide logboeken:

`act -v`

- Voer een specifieke workflow uit:

`act push -W {{pad/naar/workflow}}`
