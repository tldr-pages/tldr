# apt-add-repository

> Zarządzaj definicjami repozytoriów `apt`.
> Więcej informacji: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- Dodaj nowe repozytorium `apt`:

`apt-add-repository {{specyfikacja_repozytorium}}`

- Usuń repozytorium `apt`:

`apt-add-repository --remove {{specyfikacja_repozytorium}}`

- Zaktualizuj pamięć podręczną pakietów po dodaniu repozytorium:

`apt-add-repository --update {{specyfikacja_repozytorium}}`

- Pozwól na pobieranie pakietów źródłowych z podanego repozytorium:

`apt-add-repository --enable-source {{specyfikacja_repozytorium}}`
