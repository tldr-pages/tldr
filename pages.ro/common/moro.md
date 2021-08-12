# moro

> Urmăriți timpul de lucru.
> Mai multe informaţii: <https://moro.js.org>

- Invocați `moro `fără parametri, pentru a seta ora curentă ca începutul zilei de lucru:

`moro`

- Specificați o oră personalizată pentru începutul zilei de lucru:

`moro hi {{09:30}}`

- Invocați „moro” fără parametri a doua oară, pentru a seta ora curentă la sfârșitul zilei de lucru:

`moro`

- Specificați o oră personalizată pentru sfârșitul zilei de lucru:

`moro bye {{17:30}}`

- Adăugați o notă în ziua lucrătoare curentă:

`moro note {{3 hours on project Foo}}`

- Afișați un raport de jurnale de timp și note pentru ziua lucrătoare curentă:

`moro report`

- Afișați un raport de jurnale de timp și note pentru toate zilele lucrătoare înregistrate:

`moro report --all`
