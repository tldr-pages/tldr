# ac

> Wyświetl statystyki dotyczące czasu połączenia użytkowników.
> Więcej informacji: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Wyświetl w godzinach jak długo aktualny użytkownik był połączony:

`ac`

- Wyświetl ile godzin użytkownicy byli połączeni:

`ac {{[-p|--individual-totals]}}`

- Wyświetl ile godzin konkretny użytkownik był połączony:

`ac {{[-p|--individual-totals]}} {{użytkownik}}`

- Wyświetl ile godzin na dzień konkretny użytkownik był podłączony (z podsumowaniem):

`ac {{[-d|--daily-totals]}} {{[-p|--individual-totals]}} {{użytkownik}}`

- Wyświetlaj także dodatkowe szczegóły:

`ac --compatibility`
