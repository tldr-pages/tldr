# dotnet build

> Buduj aplikacje .NET i ich zależności.
> Więcej informacji: <https://docs.microsoft.com/dotnet/core/tools/dotnet-build>.

- Kompiluj projekt lub solucje w bieżącym katalogu:

`dotnet build`

- Kompiluj w konfiguracji debugowania:

`dotnet build {{path/to/project_or_solution}}`

- Kompiluj w konfiguracji wydania:

`dotnet build --configuration {{Release}}`

- Kompiluj bez przywracania zależności:

`dotnet build --no-restore`

- Kompiluj z wybranym poziomem szczegółowości logu:

`dotnet build --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`

- Kompiluj dla wybranego środowiska uruchomieniowego:

`dotnet build --runtime {{runtime_identifier}}`

- Kompiluj do wybranego katalogu:

`dotnet build --output {{path/to/directory}}`
