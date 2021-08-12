# kill

> Trimite un semnal la un proces, de obicei legat de oprirea procesului.
> Toate semnalele, cu excepția SIGKill și SIGSTOP, pot fi interceptate de proces pentru a efectua o ieșire curată.

- Terminarea unui program utilizând semnalul implicit SIGTERM (terminare):

`kill {{process_id}}`

- Lista denumirilor semnalelor disponibile (a se utiliza fără prefixul „SIG”):

`kill -l`

- Termină un loc de muncă de fundal:

`kill %{{job_id}}`

- Terminați un program folosind semnalul SIGHUP (închide). Mulţi demoni se vor reîncarca în loc să se termine:

`kill -{{1|HUP}} {{process_id}}`

- Terminați un program utilizând semnalul SIGINT (întrerupere). Aceasta este inițiată de obicei de către utilizatorul apăsând 'Ctrl + C`:

`kill -{{2|INT}} {{process_id}}`

- Semnal sistemul de operare pentru a termina imediat un program (care devine nici o șansă de a capta semnalul):

`kill -{{9|KILL}} {{process_id}}`

- Semnalează sistemul de operare să întrerupă un program până când este primit un semnal SIGCONT („continua”):

`kill -{{17|STOP}} {{process_id}}`

- Trimiteți un semnal `SIGUSR1` la toate procesele cu GID dat (ID grup):

`kill -{{SIGUSR1}} -{{group_id}}`
