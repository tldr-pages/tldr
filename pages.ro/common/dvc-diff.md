# dvc diff

> Afișează modificările în fișierele și directoarele urmărite DVC.
> Mai multe informaţii: <https://dvc.org/doc/command-reference/diff>

- Comparați fișierele urmărite DVC din diferite Git comite, etichete și sucursale w.r.t spațiul de lucru curent:

`dvc diff {{commit_hash/tag/branch}}`

- Comparați modificările din fișierele DVC urmărite de la 1 Git se angajează la altul:

`dvc diff {{revision_b}} {{revision_a}}`

- Comparați DVC urmărite fișiere, împreună cu cele mai recente hash lor:

`dvc diff --show-hash {{commit}}`

- Comparați fișierele urmărite DVC, afișând ieșirea ca JSON:

`dvc diff --show-json --show-hash {{commit}}`

- Comparați fișierele urmărite DVC, afișând ieșirea ca Markdown:

`dvc diff --show-md --show-hash {{commit}}`
