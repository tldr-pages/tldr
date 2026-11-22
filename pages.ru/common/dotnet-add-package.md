# dotnet add package

> Добавлять или обновлять ссылку на пакет .NET в файле проекта.
> Больше информации: <https://learn.microsoft.com/dotnet/core/tools/dotnet-add-package>.

- Добавить пакет в проект в текущем каталоге:

`dotnet add package {{пакет}}`

- Добавить пакет в конкретный проект:

`dotnet add {{путь/к/файлу.csproj}} package {{пакет}}`

- Добавить конкретную версию пакета в проект:

`dotnet add package {{пакет}} {{[-v|--version]}} {{1.0.0}}`

- Добавить пакет, используя конкретный источник NuGet:

`dotnet add package {{пакет}} {{[-s|--source]}} {{https://api.nuget.org/v3/index.json}}`

- Добавить пакет только для конкретной целевой платформы:

`dotnet add package {{пакет}} {{[-f|--framework]}} {{net7.0}}`

- Добавить пакет, указав каталог для восстановления пакетов (`~/.nuget/packages` по умолчанию):

`dotnet add package {{пакет}} --package-directory {{путь/к/каталогу}}`
