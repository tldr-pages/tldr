# rsync

> Przesyłaj pliki do lub ze zdalnego hosta (ale nie pomiędzy dwoma zdalnymi hostami), domyślnie używając SSH.
> Aby wskazać na ścieżkę zdalną, użyj `host:ścieżka/do/pliku_lub_katalogu`.
> Więcej informacji: <https://download.samba.org/pub/rsync/rsync.1>.

- Prześlij plik:

`rsync {{ścieżka/do/źródła}} {{ścieżka/do/miejsca_docelowego}}`

- Użyj trybu archiwum (rekursywnie kopiuj katalogi, kopiuj dowiązania symboliczne bez rozwiązywania i zachowaj uprawnienia, własność i czasy modyfikacji):

`rsync --archive {{ścieżka/do/źródła}} {{ścieżka/do/miejsca_docelowego}}`

- Kompresuj dane podczas gdy są wysyłane do miejsca docelowego, wyświetlaj szczegółowy i czytelny dla człowieka postęp i zachowaj częściowo przesłane pliki w przypadku przerwania:

`rsync --compress --verbose --human-readable --partial --progress {{ścieżka/do/źródła}} {{ścieżka/do/miejsca_docelowego}}`

- Rekursywnie kopiuj katalogi:

`rsync --recursive {{ścieżka/do/źródła}} {{ścieżka/do/miejsca_docelowego}}`

- Prześlij zawartość katalogu, ale nie sam katalog:

`rsync --recursive {{ścieżka/do/źródła}}/ {{ścieżka/do/miejsca_docelowego}}`

- Rekursywnie kopiuj katalogi, użyj trybu archiwum, rozwiąż dowiązania symboliczne i pomiń pliki, które są nowsze w miejscu docelowym:

`rsync --archive --update --copy-links {{ścieżka/do/źródła}} {{ścieżka/do/miejsca_docelowego}}`

- Prześlij katalog do zdalnego hosta, na którym działa `rsyncd` i usuń pliki w miejscu docelowym które nie istnieją w źródle:

`rsync --recursive --delete rsync://{{host}}:{{ścieżka/do/źródła}} {{ścieżka/do/miejsca_docelowego}}`

- Prześlij plik poprzez SSH używając innego portu niż domyślny (22) i wyświetlaj globalny postęp:

`rsync --rsh 'ssh -p {{port}}' --info=progress2 {{host}}:{{ścieżka/do/źródła}} {{ścieżka/do/miejsca_docelowego}}`
