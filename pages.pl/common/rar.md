# rar

> Archiwizator RAR. Obsługuje wielotomowe archiwa, które mogą być opcjonalnie samorozpakowujące się.
> Więcej informacji: <https://manned.org/rar>.

- Zarchiwizuj 1 lub więcej plików:

`rar a {{ścieżka/do/nazwa_archiwum.rar}} {{ścieżka/do/pliku1}} {{ścieżka/do/pliku2}} {{ścieżka/do/pliku3}}`

- Zarchiwizuj katalog:

`rar a {{ścieżka/do/nazwa_archiwum.rar}} {{ścieżka/do/katalogu}}`

- Podziel archiwum na części równej wielkości (50M):

`rar a -v{{50M}} -R {{ścieżka/do/nazwa_archiwum.rar}} {{ścieżka/do/pliku_lub_katalogu}}`

- Chroń hasłem powstające archiwum:

`rar a -p{{hasło}} {{ścieżka/do/nazwa_archiwum.rar}} {{ścieżka/do/pliku_lub_katalogu}}`

- Szyfruj dane pliku i ich nagłówki za pomocą hasła:

`rar a -hp{{hasło}} {{ścieżka/do/nazwa_archiwum.rar}} {{ścieżka/do/pliku_lub_katalogu}}`

- Użyj określonego poziomu kompresji (0-5):

`rar a -m{{poziom_kompresji}} {{ścieżka/do/nazwa_archiwum.rar}} {{ścieżka/do/pliku_lub_katalogu}}`
