# git blame

> Wyświetl commit i ostatniego autora każdej linii pliku.
> Więcej informacji: <https://git-scm.com/docs/git-blame>.

- Wyświetl plik z informacjami o autorstwie (nazwa autora i hash commitu):

`git blame {{ścieżka/do/pliku}}`

- Wyświetl e-mail autora zamiast nazwy:

`git blame {{[-e|--show-email]}} {{ścieżka/do/pliku}}`

- Wyświetl plik z informacjami o autorstwie dla określonego commitu:

`git blame {{commit}} {{ścieżka/do/pliku}}`

- Wyświetl plik z informacjami o autorstwie przed określonym commitem:

`git blame {{commit}}~ {{ścieżka/do/pliku}}`

- Wyświetl plik z informacjami o autorstwie począwszy od danej linii:

`git blame -L {{123}} {{ścieżka/do/pliku}}`

- Adnotuj określony zakres linii pliku:

`git blame -L {{linia_początkowa}},{{linia_końcowa}} {{ścieżka/do/pliku}}`

- Adnotuj 10 linii pliku poczynając od pierwszej linii pasującej do podanego tekstu:

`git blame -L '/{{tekst}}/',+10 {{ścieżka/do/pliku}}`

- Adnotuj plik ignorując białe znaki i przenoszenia linii:

`git blame -w -C -C -C {{ścieżka/do/pliku}}`
