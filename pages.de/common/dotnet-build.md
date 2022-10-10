# dotnet build

> Baut eine .NET Anwendung und ihre Abhängigkeiten.
> Weitere Informationen: <https://learn.microsoft.com/de-de/dotnet/core/tools/dotnet-build>.

- Kompiliert das Projekt oder eine Projektmappendatei in dem aktuellen Ordner:

`dotnet build`

- Kompiliert ein .NET Projekt oder eine Projektmappendatei Debug-Modus:

`dotnet build {{path/to/project_or_solution}}`

- Kompiliert m Release-Modus:

`dotnet build --configuration {{Release}}`

- Kompiliert ohne die Abhängigkeiten wiederherzustellen:

`dotnet build --no-restore`

- Kompiliert mit einem spezifische Ausführlichkeitsgrad:

`dotnet build --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`

- Kompiliert für eine spezifische Laufzeitumgebung:

`dotnet build --runtime {{runtime_identifier}}`

- Kompiliert in ein spezifischen Ordner:

`dotnet build --output {{path/to/directory}}`
