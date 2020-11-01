# rm

> Usuwa pliki lub foldery.

- Usuń pliki z dowolnej lokalizacji:

`rm {{ścieżka/do/pliku}} {{ścieżka/do/innego/pliku}}`

- Rekursywnie usuń folder oraz wszystkie jego podfoldery:

`rm -r {{ścieżka/do/folderu}}`

- Wymuś usunięcie folderu, bez pytania o potwierdzenie lub pokazywania błędów:

`rm -rf {{ścieżka/do/folderu}}`

- Interaktywnie usuń kilka plików z pytaniem o potwierdzenie przed każdym usunięciem:

`rm -i {{plik(i)}}`

- Usuń pliki w trybie opisowym, pokazując wiadomość o każdym usuniętym pliku:

`rm -v {{ścieżka/do/folderu/*}}`
