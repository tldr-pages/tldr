# hub

> A Git csomagolása, amely parancsokat ad hozzá a GitHub-alapú projektekkel való munkához. Ha a `hub alias` utasításai szerint van beállítva, akkor a `git` segítségével a `hub` parancsokat lehet futtatni. További információ: <https://hub.github.com>.

- Klónozhat egy tárolót a slugja segítségével (a tulajdonosok kihagyhatják a felhasználónevet):

`hub clone {{username}}/{{repo_name}}`

- Az aktuális (egy másik felhasználótól klónozott) tárolóhely elágazásának létrehozása a GitHub profilja alatt:

`hub fork`

- Tolja az aktuális helyi ágat a GitHubra, és hozzon létre egy PR-t az eredeti tárolóban:

`hub push {{remote_name}} && hub pull-request`

- Hozzon létre egy PR-t az aktuális (már elküldött) ágról, újra felhasználva az első commit üzenetét:

`hub pull-request --no-edit`

- Hozzon létre egy új ágat egy pull request tartalmával, és váltson rá:

`hub pr checkout {{pr_number}}`

- Töltse fel az aktuális (csak helyi) tárolót a GitHub-fiókjába:

`hub create`

- Git-objektumok lekérése az upstreamről és a helyi ágak frissítése:

`hub sync`
