# strace

> Instrument de depanare pentru urmărirea apelurilor de sistem.

- Începeți urmărirea unui anumit proces prin PID-ul său:

`strace -p {{pid}}`

- Urmăriți un proces și filtrați ieșirea prin apel de sistem:

`strace -p {{pid}} -e {{system_call_name}}`

- Numărați timpul, apelurile și erorile pentru fiecare apel de sistem și raportați un rezumat la ieșirea programului:

`strace -p {{pid}} -c`

- Afișați timpul petrecut în fiecare apel de sistem:

`strace -p {{pid}} -T`

- Începeți urmărirea unui program prin executarea acestuia:

`strace {{program}}`

- Începeți urmărirea operațiunilor de fișier ale unui program:

`strace -e trace=file {{program}}`
