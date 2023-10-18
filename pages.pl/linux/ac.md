# ac

> Wyświetla statystyki jak długo użytkownicy byli podłączeni.
> Więcej informacji: <https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- Wyświetenie informacji w godzinach jak długo aktualny użytkownik był podłączony:

`ac`

- Wyświetlenie ile godzin użytkownicy byli podłączeni:

`ac --individual-totals`

- Wyświetlenie ile godzin konkretny użytkownik był podłączony:

`ac --individual-totals {{użytkownik}}`

- Wyświetlenie ile godzin per dzień konkretny użytkownik był podłączony (z podsumowaniem):

`ac --daily-totals --individual-totals {{użytkownik}}`

- Także wyświetlaj dodatkowe szczegóły:

`ac --compatibility`
