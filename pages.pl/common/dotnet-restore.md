# dotnet restore

> Przywracanie zależności i narzędzi dla projektu .NET.
> Więcej informacji: <https://learn.microsoft.com/dotnet/core/tools/dotnet-restore>.

- Przywróć zależności dla projektu lub solucji w bieżącym katalogu:

`dotnet restore`

- Przywróć zależności dla projektu lub solucji w wybranym katalogu:

`dotnet restore {{ścieżka/do/projektu_lub_solucji}}`

- Przywróć zależnośći pomijając cache zapytań HTTP:

`dotnet restore --no-cache`

- Wymuś rozwiązanie wszystkich zależności nawet jeśli poprzednie przywracanie zakończyło się sukcesem:

`dotnet restore --force`

- Ignoruj błędy w trakcie przywracania zależności ze źródeł:

`dotnet restore --ignore-failed-sources`

- Przywróć zależności z wybranym poziomem szczegółowości logów:

`dotnet restore --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`
