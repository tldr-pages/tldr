# choco list

> Wyświetlanie listy pakietów Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-list>.

- Wyświetlanie wszystkich dostępnych pakietów:

`choco list`

- Wyświetlanie wszystkich lokalnie zainstalowanych pakietów:

`choco list --local-only`

- Wyświetlanie listy pakietów zawierającej lokalnie zainstalowane programy:

`choco list --include-programs`

- Wyświetlanie listy wyłącznie zatwierdzonych pakietów:

`choco list --approved-only`

- Wyświetlanie listy pakietów dpstępnych w podanym źródle/repozytorium:

`choco list --source {{adres_url|alias}}`

- PPodanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco list --user {{nazwa_użytkownika}} --password {{hasło}}`
