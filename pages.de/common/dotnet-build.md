# dotnet build

> Baue .NET Anwendungen und ihre Abhängigkeiten.
> Weitere Informationen: <https://learn.microsoft.com/de-de/dotnet/core/tools/dotnet-build>.

- Kompiliert das Projekt oder eine Projektmappendatei in dem aktuellen Ordner:

`dotnet build`

- Kompiliert ein .NET Projekt oder eine Projektmappendatei Debug-Modus:

`dotnet build {{pfad/zu/projekt_oder_projektmappendatei}}`

- Kompiliere im Release-Modus:

`dotnet build --configuration {{Release}}`

- Kompiliert ohne die Abhängigkeiten wiederherzustellen:

`dotnet build --no-restore`

- Kompiliert mit einem spezifische Ausführlichkeitsgrad:

`dotnet build --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`

- Kompiliert für eine spezifische Laufzeitumgebung:

`dotnet build --runtime {{Laufzeitbezeichner}}`

- Kompiliert in ein spezifischen Ordner:

`dotnet build --output {{pfad/zu/verzeichnis}}`
