# rsync

> Przesyłaj pliki do lub ze zdalnego hosta (ale nie pomiędzy dwoma zdalnymi hostami).
> Może przesyłać pojedyncze pliki lub wiele plików pasujących do wzorca.
> Więcej informacji: <https://manned.org/rsync>.

- Prześlij plik z lokalnego do zdalnego hosta:

`rsync {{ścieżka/do/lokalnego_pliku}} {{zdalny_host}}:{{ścieżka/do/zdalnego_katalogu}}`

- Prześlij plik ze zdalnego do lokalnego hosta:

`rsync {{zdalny_host}}:{{ścieżka/do/zdalnego_pliku}} {{ścieżka/do/lokalnego_katalogu}}`

- Prześlij plik w trybie [a]rchiwum (aby zachować atrybuty) i skompresowanym ([z]ip) wyświetlając szczegółowy ([v]erbose) i czytelny dla człowieka ([h]uman-readable) [P]ostęp:

`rsync -azvhP {{ścieżka/do/lokalnego_pliku}} {{zdalny_host}}:{{ścieżka/do/zdalnego_katalogu}}`

- Prześlij katalog i jego zawartość ze zdalnego do lokalnego hosta:

`rsync -r {{zdalny_host}}:{{ścieżka/do/zdalnego_katalogu}} {{ścieżka/do/lokalnego_katalogu}}`

- Prześlij zawartość katalogu (ale nie sam katalog) ze zdalnego do lokalnego hosta:

`rsync -r {{zdalny_host}}:{{ścieżka/do/zdalnego_katalogu}}/ {{ścieżka/do/lokalnego_katalogu}}`

- Prześlij katalog [r]ekursywnie, w trybie [a]rchiwum (aby zachować atrybuty), rozwiązując zawarte dowiązania symbo[L]iczne, i ignorując już przesłane pliki o ile nie są nowsze ([u]nless):

`rsync -rauL {{zdalny_host}}:{{ścieżka/do/zdalnego_katalogu}} {{ścieżka/do/lokalnego_katalogu}}`

- Prześlij plik poprzez SSH i usuń pliki na zdalnym hoście, które nie istnieją na lokalnym:

`rsync -e ssh --delete {{zdalny_host}}:{{ścieżka/do/zdalnego_pliku}} {{ścieżka/do/lokalnego_pliku}}`

- Prześlij pliki poprzez SSH używając innego portu niż domyślny i wyświetlaj globalny postęp:

`rsync -e 'ssh -p {{port}}' --info=progress2 {{zdalny_host}}:{{ścieżka/do/zdalnego_pliku}} {{ścieżka/do/lokalnego_pliku}}`
