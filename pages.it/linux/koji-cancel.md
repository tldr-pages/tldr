# koji cancel

> Annulla attività attive in esecuzione nel sistema di build Koji.
> Maggiori informazioni: <https://docs.pagure.org/koji/>.

- Annulla un'attività tramite il suo ID:

`koji cancel {{id_attivita}}`

- Annulla più attività:

`koji cancel {{id_attivita1 id_attivita2 ...}}`

- Annulla un'attività con output verboso:

`koji cancel --verbose {{id_attivita}}`

- Mostra aiuto:

`koji cancel {{[-h|--help]}}`
