# choco list

> Wyświetlanie listy pakietów Chocolatey.
> Więcej informacji: <https://docs.chocolatey.org/en-us/choco/commands/list/>.

- Wyświetlanie wszystkich dostępnych pakietów:

`choco list`

- Wyświetlanie wszystkich lokalnie zainstalowanych pakietów:

`choco list --local-only`

- Wyświetlanie listy pakietów zawierającej lokalnie zainstalowane programy:

`choco list {{[-i|--include-programs]}}`

- Wyświetlanie listy wyłącznie zatwierdzonych pakietów:

`choco list --approved-only`

- Wyświetlanie listy pakietów dpstępnych w podanym źródle/repozytorium:

`choco list {{[-s|--source]}} {{adres_url|alias}}`

- PPodanie nazwy użytkownika i hasła do uwierzytelnienia:

`choco list --user {{nazwa_użytkownika}} --password {{hasło}}`
