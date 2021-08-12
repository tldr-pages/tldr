# git show

> Afișați diferite tipuri de obiecte Git (angajamente, etichete etc.).
> Mai multe informaţii: <https://git-scm.com/docs/git-show>

- Afișați informații despre cea mai recentă comitere (hash, mesaj, modificări și alte metadate):

`git show`

- Afișați informații despre o anumită comitere:

`git show {{commit}}`

- Afișați informații despre comiterea asociată cu o anumită etichetă:

`git show {{tag}}`

- Afișați informații despre a treia angajare de la HEAD unei sucursale:

`git show {{branch}}~{{3}}`

- Afișați mesajul unui comitere într-o singură linie, suprimând ieșirea diff:

`git show --oneline -s {{commit}}`

- Afișați numai statistici (caractere adăugate/eliminate) despre fișierele modificate:

`git show --stat {{commit}}`

- Afișați numai lista fișierelor adăugate, redenumite sau șterse:

`git show --summary {{commit}}`

- Afișați conținutul unui fișier așa cum a fost la o anumită revizuire (de exemplu, sucursală, etichetă sau comitere):

`git show {{revision}}:{{path/to/file}}`
