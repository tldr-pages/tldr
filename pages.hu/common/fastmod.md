# fastmod

> A codemod eszköz gyors részleges cseréje, a teljes kódbázisban a replace és replace all. A regexeket a Rust regex crate illeszti össze. További információ: <https://github.com/facebookincubator/fastmod>.

- Egy regex minta cseréje az aktuális könyvtár összes fájljában, figyelmen kívül hagyva a .ignore és .gitignore fájlokat:

`fastmod {{regex_pattern}} {{replacement}}`

- Egy regex minta cseréje nagy- és kisbetűket nem érzékelő üzemmódban meghatározott fájlokban vagy könyvtárakban:

`fastmod --ignore-case {{regex_pattern}} {{replacement}} -- {{path/to/file path/to/directory ...}}`

- Egy regex minta cseréje egy adott könyvtárban a nagy- és kisbetű-érzékeny glob mintával szűrt fájlokban:

`fastmod {{regex}} {{replacement}} --dir {{path/to/directory}} --iglob {{'**/*.{js,json}'}}`

- Pontos karakterlánc cseréje .js vagy .json fájlokban:

`fastmod --fixed-strings {{exact_string}} {{replacement}} --extensions {{json,js}}`

- Csere pontos karakterláncra megerősítés kérése nélkül (a reguláris kifejezések kikapcsolása):

`fastmod --accept-all --fixed-strings {{exact_string}} {{replacement}}`

- Pontos karakterlánc cseréje megerősítés kérése nélkül, a módosított fájlok nyomtatása:

`fastmod --accept-all --print-changed-files --fixed-strings {{exact_string}} {{replacement}}`
