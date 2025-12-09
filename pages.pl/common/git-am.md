# git am

> Zastosuj pliki poprawki i utwórz commit. Przydatne przy otrzymywaniu commitów przez email.
> Zobacz także `git format-patch`, który może generować pliki poprawki.
> Więcej informacji: <https://git-scm.com/docs/git-am>.

- Zastosuj i komituj zmiany z lokalnego pliku poprawki:

`git am {{ścieżka/do/pliku.patch}}`

- Zastosuj i komituj zmiany ze zdalnego pliku poprawki:

`curl {{[-L|--location]}} {{https://example.com/plik.patch}} | git apply`

- Przerwij proces zastosowania pliku poprawki:

`git am --abort`

- Zastosuj jak największą część pliku poprawki, zapisując nieudane fragmenty w plikach odrzuceń (pliki `.rej`):

`git am --reject {{ścieżka/do/pliku.patch}}`
