# dotnet tool

> Zarządzaj narzędziami .NET i szukaj narzędzi opublikowanych w repozytorium NuGet.
> Więcej informacji: <https://learn.microsoft.com/dotnet/core/tools/global-tools>.

- Zainstaluj narzędzie globalne (nie używaj flagi `--global` by użyć polecenia dla narzędzi lokalnych):

`dotnet tool install --global {{dotnetsay}}`

- Zainstaluj narzędzia zdefiniowane w lokalnym manifeście narzędzi:

`dotnet tool restore`

- Zaktualizuj wyspecyfikowane narzędzie globalne (nie używaj flagi `--global` by użyć polecenia dla narzędzi lokalnych):

`dotnet tool update --global {{tool_name}}`

- Odinstaluj narzędzie globalne (nie używaj flagi `--global` by użyć polecenia dla narzędzi lokalnych):

`dotnet tool uninstall --global {{tool_name}}`

- Wyświetl zainstalowane narzędzia globalne (nie używaj flagi `--global` by użyć polecenia dla narzędzi lokalnych):

`dotnet tool list --global`

- Szukaj narzędzi w repozytorium NuGet:

`dotnet tool search {{search_term}}`

- Wyświetl pomoc:

`dotnet tool --help`
