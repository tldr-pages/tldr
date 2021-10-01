# dotnet

> Plattformübergreifende Kommandozeilenandwendungen für .NET Core.
> Manche Unterbefehle wie `dotnet build` sind separat dokumentiert.
> Weitere Informationen: <https://docs.microsoft.com/dotnet/core/tools>.

- Initialisiere ein neues .NET Projekt:

`dotnet new {{vorlagen_name}}`

- Stelle nuget-Pakete wieder her:

`dotnet restore`

- Baue des .NET Projekt im aktuellen Ordner und führe es aus:

`dotnet run`

- Führe eine gebaute dotnet-Applikation aus (Benötigt nur die Laufzeitumgebung. Die anderen Befehle benötigen auch den Entwicklungsteil):

`dotnet {{pfad/zu/anwendung.dll}}`
