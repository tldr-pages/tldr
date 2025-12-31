# add-apt-repository

> Zarządzaj definicjami repozytoriów `apt`.
> Więcej informacji: <https://manned.org/add-apt-repository>.

- Dodaj nowe repozytorium `apt`:

`add-apt-repository {{specyfikacja_repozytorium}}`

- Usuń repozytorium `apt`:

`add-apt-repository {{[-r|--remove]}} {{specyfikacja_repozytorium}}`

- Zaktualizuj pamięć podręczną pakietów po dodaniu repozytorium:

`add-apt-repository --update {{specyfikacja_repozytorium}}`

- Pozwól na pobieranie pakietów źródłowych z podanego repozytorium:

`add-apt-repository {{[-s|--enable-source]}} {{specyfikacja_repozytorium}}`
