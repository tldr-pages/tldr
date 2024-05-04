# svccfg

> Importowanie, eksportowanie i modyfikowanie konfiguracji usług.
> Więcej informacji: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Sprawdzenie poprawności pliku konfiguracyjnego:

`svccfg validate {{sciezka/do/pliku_smf.xml}}`

- Eksport konfiguracji usług do pliku:

`svccfg export {{nazwauslugi}} > {{sciezka/do/pliku_smf.xml}}`

- Importowanie/aktualizowanie konfiguracji usług z pliku:

`svccfg import {{sciezka/do/pliku_smf.xml}}`
