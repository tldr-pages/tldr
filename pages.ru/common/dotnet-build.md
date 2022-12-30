# dotnet build

> Собирает приложение .NET и все его зависимости.
> Больше информации: <https://learn.microsoft.com/dotnet/core/tools/dotnet-build>.

- Скомпилировать проект или решение в текущей директории:

`dotnet build`

- Скомпилировать проект или решение .NET в режиме debug:

`dotnet build {{путь/до/проекта_или_решения}}`

- Скомпилировать в режиме release:

`dotnet build --configuration {{Release}}`

- Скомпилировать без восстановления зависимостей:

`dotnet build --no-restore`

- Скомпилировать с заданным уровнем детализации выводимой информации:

`dotnet build --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`

- Скомпилировать для заданной среды исполнения:

`dotnet build --runtime {{идентификатор_среды_исполения}}`

- Указать целевую папку:

`dotnet build --output {{путь/до/папки}}`
