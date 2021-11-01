# todo

> Un semplice gestore per i todo da linea di comando.
> Maggiori informazioni: <https://todoman.readthedocs.io>.

- Elenco dei task che possono essere inizializzati:

`todo list --startable`

- Aggiungere un nuovo task alla lista delle cose da fare per lavoro:

`todo new {{cose_da_fare}} --list {{lavoro}}`

- Aggiungere una località ad un task con un dato ID:

`todo edit --location {{nome_località}} {{task_id}}`

- Mostrare i dettagli di un task:

`todo show {{task_id}}`

- Contrassegnare un task con un ID specifico come completato:

`todo done {{task_id1 task_id2 ...}}`

- Eliminare un task:

`todo delete {{task_id}}`

- Eliminare un task completato e ripristinare gli ID dei task rimanenti:

`todo flush`
