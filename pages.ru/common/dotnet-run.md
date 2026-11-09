# dotnet run

> Запускать приложение .NET без явных команд компиляции или запуска.
> Больше информации: <https://learn.microsoft.com/dotnet/core/tools/dotnet-run>.

- Запустить проект в текущем каталоге:

`dotnet run`

- Запустить конкретный проект:

`dotnet run --project {{путь/к/файлу.csproj}}`

- Запустить проект с конкретными аргументами:

`dotnet run -- {{аргумент1=foo аргумент2=bar ...}}`

- Запустить проект, используя моникер целевой платформы:

`dotnet run {{[-f|--framework]}} {{net7.0}}`

- Указать архитектуру и ОС, доступно начиная с .NET 6 (не используйте `--runtime` с этими параметрами):

`dotnet run {{[-a|--arch]}} {{x86|x64|arm|arm64}} --os {{win|win7|osx|linux|ios|android}}`
