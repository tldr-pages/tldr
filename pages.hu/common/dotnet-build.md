# dotnet build

> .NET-alkalmazást és függőségeit építi. További információ: <https://learn.microsoft.com/dotnet/core/tools/dotnet-build>.

- Az aktuális könyvtárban lévő projekt vagy megoldás fordítása:

`dotnet build`

- .NET projekt vagy megoldás fordítása hibakeresési módban:

`dotnet build {{path/to/project_or_solution}}`

- Fordítás kiadás üzemmódban:

`dotnet build --configuration {{Release}}`

- Kompilálás függőségek visszaállítása nélkül:

`dotnet build --no-restore`

- Kompilálás egy adott szóbeliségi szinttel:

`dotnet build --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`

- Kompilálás egy adott futási időre:

`dotnet build --runtime {{runtime_identifier}}`

- A kimeneti könyvtár megadása:

`dotnet build --output {{path/to/directory}}`
