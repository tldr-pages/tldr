# linkchecker

> Parancssori kliens HTML dokumentumok és weboldalak törött linkek ellenőrzésére. További információ: <https://linkchecker.github.io/linkchecker/>.

- Törött linkek keresése a https://example.com/ oldalon:

`linkchecker {{https://example.com/}}`

- Ellenőrizze a külső tartományokra mutató URL-címeket is:

`linkchecker --check-extern {{https://example.com/}}`

- Figyelmen kívül hagyhatja azokat az URL-címeket, amelyek megfelelnek egy adott reguláris kifejezésnek:

`linkchecker --ignore-url {{regular_expression}} {{https://example.com/}}`

- Az eredmények CSV fájlba történő kimenete:

`linkchecker --file-output {{csv}}/{{path/to/file}} {{https://example.com/}}`
