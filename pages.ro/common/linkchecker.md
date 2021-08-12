# linkchecker

> Client de linie de comandă pentru a verifica documente HTML și site-uri web pentru linkuri întrerupte.
> Mai multe informaţii: <https://linkchecker.github.io/linkchecker/>

- Găsiți link-uri rupte pe https://example.com/:

`linkchecker {{https://example.com/}}`

- De asemenea, verificați URL-urile care indică spre domenii externe:

`linkchecker --check-extern {{https://example.com/}}`

- Ignorați adresele URL care se potrivesc cu o anumită expresie regulată:

`linkchecker --ignore-url {{regular_expression}} {{https://example.com/}}`

- Rezultatele de ieșire într-un fișier CSV:

`linkchecker --file-output {{csv}}/{{path/to/file}} {{https://example.com/}}`
