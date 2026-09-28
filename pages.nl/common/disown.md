# disown

> Zorg ervoor dat subprocessen kunnen blijven bestaan nadat de shell waaraan ze gekoppeld zijn, is afgesloten.
> Zie ook: `jobs`.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-disown>.

- Ontkoppel de huidige job:

`disown`

- Ontkoppel een specifieke job (voer `jobs` uit om het jobnummer te vinden):

`disown %{{job_number}}`

- Ontkoppel alle jobs (alleen Bash):

`disown -a`

- Behoud de job (ontkoppel deze niet), maar markeer deze zodat er geen toekomstige SIGHUP wordt ontvangen bij het afsluiten van de shell (alleen Bash):

`disown -h %{{job_number}}`
