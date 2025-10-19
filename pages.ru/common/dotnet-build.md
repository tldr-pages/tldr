# dotnet build

> Собирает приложение .NET и все его зависимости.
> Больше информации: <https://learn.microsoft.com/dotnet/core/tools/dotnet-build>.

- Скомпилировать проект или решение в текущем каталоге:

`dotnet build`

- Скомпилировать проект или решение .NET в режиме debug:

`dotnet build {{путь/к/проекту_или_решению}}`

- Скомпилировать в режиме release:

`dotnet build {{[-c|--configuration]}} {{Release}}`

- Скомпилировать без восстановления зависимостей:

`dotnet build --no-restore`

- Скомпилировать с заданным уровнем детализации выводимой информации:

`dotnet build {{[-v|--verbosity]}} {{quiet|minimal|normal|detailed|diagnostic}}`

- Скомпилировать для заданной среды исполнения:

`dotnet build {{[-r|--runtime]}} {{идентификатор_среды_исполнения}}`

- Указать целевой каталог:

`dotnet build {{[-o|--output]}} {{путь/к/каталогу}}`
