# killall

> Trimite semnal de ucidere la toate instanțele unui proces după nume (trebuie să fie numele exact).
> Toate semnalele cu excepția SIGKill și SIGSTOP pot fi interceptate de proces, permițând o ieșire curată.

- Terminați un proces utilizând semnalul implicit SIGTERM (terminați):

`killall {{process_name}}`

- Lista denumirilor semnalelor disponibile (pentru a fi utilizate fără prefixul „SIG”):

`killall --list`

- Cereți interactiv confirmarea înainte de reziliere:

`killall -i {{process_name}}`

- Terminați un proces utilizând semnalul SIGINT (întrerupere), care este același semnal trimis prin apăsarea 'Ctrl + C`:

`killall -INT {{process_name}}`

- Forța ucide un proces:

`killall -KILL {{process_name}}`
