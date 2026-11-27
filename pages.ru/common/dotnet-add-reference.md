# dotnet add reference

> Добавлять межпроектные ссылки .NET.
> Больше информации: <https://learn.microsoft.com/dotnet/core/tools/dotnet-add-reference>.

- Добавить ссылку в проект в текущем каталоге:

`dotnet add reference {{путь/к/ссылке.csproj}}`

- Добавить несколько ссылок в проект в текущем каталоге:

`dotnet add reference {{путь/к/ссылке1.csproj путь/к/ссылке2.csproj ...}}`

- Добавить ссылку в конкретный проект:

`dotnet add {{путь/к/проекту.csproj}} reference {{путь/к/ссылке.csproj}}`

- Добавить несколько ссылок в конкретный проект:

`dotnet add {{путь/к/проекту.csproj}} reference {{путь/к/ссылке1.csproj путь/к/ссылке2.csproj ...}}`
