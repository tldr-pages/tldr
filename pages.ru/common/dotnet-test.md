# dotnet test

> Выполнять тесты для приложения .NET.
> Примечание: см. <https://learn.microsoft.com/dotnet/core/testing/selective-unit-tests> для поддерживаемых выражений фильтрации.
> Больше информации: <https://learn.microsoft.com/dotnet/core/tools/dotnet-test>.

- Выполнить тесты для проекта/решения .NET в текущем каталоге:

`dotnet test`

- Выполнить тесты для проекта/решения .NET по указанному пути:

`dotnet test {{путь/к/проекту_или_решению}}`

- Выполнить тесты, соответствующие заданному выражению фильтрации:

`dotnet test --filter {{Name~TestMethod1}}`
