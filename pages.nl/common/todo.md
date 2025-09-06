# todo

> Een eenvoudige, op standaarden gebaseerde, opdrachtregel todo manager.
> Meer informatie: <https://todoman.readthedocs.io>.

- Toon startbare taken:

`todo list --startable`

- Voeg een nieuwe taak toe aan de werklijst:

`todo new {{ding_om_te_doen}} --list {{werk}}`

- Voeg een locatie toe aan een taak met een gegeven ID:

`todo edit --location {{locatie_naam}} {{taak_id}}`

- Toon details over een taak:

`todo show {{taak_id}}`

- Markeer taken met de opgegeven IDs als voltooid:

`todo done {{taak_id1 taak_id2 ...}}`

- Verwijder een taak:

`todo delete {{taak_id}}`

- Verwijder voltooide taken en reset de IDs van de overgebleven taken:

`todo flush`
