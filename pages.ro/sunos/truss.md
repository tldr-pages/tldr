# truss

> Instrument de depanare pentru urmărirea apelurilor de sistem.
> Echivalentul SunOS pentru strace.
> Mai multe informații: <https://www.unix.com/man-page/linux/1/truss>.

- Începe urmărirea unui program prin executarea acestuia, urmărind toate procesele copil:

`truss -f {{program}}`

- Începe urmărirea unui proces specific după PID-ul său:

`truss -p {{pid}}`

- Începe urmărirea unui program prin executarea acestuia, afișând argumentele și variabilele de mediu:

`truss -a -e {{program}}`

- Numără timpul, apelurile și erorile pentru fiecare apel de sistem și raportează un rezumat la ieșirea programului:

`truss -c -p {{pid}}`

- Urmărește un proces filtrând ieșirea după apelul de sistem:

`truss -p {{pid}} -t {{nume_apel_sistem}}`