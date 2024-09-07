# svccfg

> Importuj, eksportuj i modyfikuj konfigurację usług.
> Więcej informacji: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Sprawdź poprawność pliku konfiguracyjnego:

`svccfg validate {{ścieżka/do/pliku_smf.xml}}`

- Eksportuj konfigurację usług do pliku:

`svccfg export {{nazwa_usługi}} > {{ścieżka/do/pliku_smf.xml}}`

- Importuj/aktualizuj konfigurację usług z pliku:

`svccfg import {{ścieżka/do/pliku_smf.xml}}`
