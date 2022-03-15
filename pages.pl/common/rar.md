# rar

> Archiwizator RAR. Obsługuje wielotomowe archiwa, które mogą być opcjonalnie samorozpakowujące się.
> Więcej informacji: <https://manned.org/rar>.

- Zarchiwizuj 1 lub więcej plików:

`rar a {{sciezka/do/nazwa_archiwum.rar}} {{sciezka/do/plik1}} {{sciezka/do/plik2}} {{sciezka/do/plik3}}`

- Zarchiwizuj katalog:

`rar a {{sciezka/do/nazwa_archiwum.rar}} {{sciezka/do/katalog}}`

- Podziel archiwum na części równej wielkości (50M):

`rar a -v{{50M}} -R {{sciezka/do/nazwa_archiwum.rar}} {{sciezka/do/plik_lub_katalog}}`

- Chroń hasło wynikowego archiwum:

`rar a -p{{haslo}} {{sciezka/do/nazwa_archiwum.rar}} {{sciezka/do/plik_lub_katalog}}`

- Szyfruj dane pliku i nagłówki za pomocą hasła:

`rar a -hp{{haslo}} {{sciezka/do/nazwa_archiwum.rar}} {{sciezka/do/plik_lub_katalog}}`

- Użyj określonego poziomu kompresji (0-5):

`rar a -m{{poziom_kompresji}} {{sciezka/do/nazwa_archiwum.rar}} {{sciezka/do/plik_lub_katalog}}`
