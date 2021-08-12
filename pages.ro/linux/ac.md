# ac

> Imprimare statistici cu privire la durata conectării utilizatorilor.
> Mai multe informaţii: <https://www.gnu.org/software/acct/manual/accounting.html#ac>

- Imprimați cât timp utilizatorul curent a fost conectat în ore:

`ac`

- Imprimați cât timp utilizatorii au fost conectați în ore:

`ac --individual-totals`

- Imprimați cât timp un anumit utilizator a fost conectat în ore:

`ac --individual-totals {{username}}`

- Imprimați cât timp un anumit utilizator a fost conectat în ore pe zi (cu total):

`ac --daily-totals --individual-totals {{username}}`

- Afișați, de asemenea, detalii suplimentare:

`ac --compatibility`
