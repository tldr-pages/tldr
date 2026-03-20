# dotnet build

> Buduj aplikacje .NET i ich zależności.
> Więcej informacji: <https://learn.microsoft.com/dotnet/core/tools/dotnet-build>.

- Kompiluj projekt lub solucje w bieżącym katalogu:

`dotnet build`

- Kompiluj w konfiguracji debugowania:

`dotnet build {{ściezka/do/projektu_lub_solucji}}`

- Kompiluj w konfiguracji wydania:

`dotnet build {{[-c|--configuration]}} {{Release}}`

- Kompiluj bez przywracania zależności:

`dotnet build --no-restore`

- Kompiluj z wybranym poziomem szczegółowości logu:

`dotnet build {{[-v|--verbosity]}} {{quiet|minimal|normal|detailed|diagnostic}}`

- Kompiluj dla wybranego środowiska uruchomieniowego:

`dotnet build {{[-r|--runtime]}} {{identyfikator_runtime}}`

- Kompiluj do wybranego katalogu:

`dotnet build {{[-o|--output]}} {{ścieżka/do/katalogu}}`
