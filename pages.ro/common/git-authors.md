# git authors

> Generează o listă cu commitatorii unui repository Git.
> Parte din `git-extras`.
> Mai multe informații: <https://manned.org/git-authors>.

- Afișează o listă completă cu commitatorii la `stdout` în loc de fișierul `AUTHORS`:

`git authors {{[-l|--list]}}`

- Adaugă lista de commitatori la fișierul `AUTHORS` și îl deschide în editorul implicit:

`git authors`

- Adaugă lista de commitatori, excluzând email-urile, la fișierul `AUTHORS` și îl deschide în editorul implicit:

`git authors --no-email`
