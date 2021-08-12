# dotnet build

> Construiește o aplicație NET și dependențele sale.
> Mai multe informaţii: <https://docs.microsoft.com/dotnet/core/tools/dotnet-build>

- Compilați proiectul sau soluția în directorul curent:

`dotnet build`

- Compilați un proiect sau o soluție NET în modul de depanare:

`dotnet build {{path/to/project_or_solution}}`

- Compilare în modul de eliberare:

`dotnet build --configuration {{Release}}`

- Compilați fără a restabili dependențele:

`dotnet build --no-restore`

- Compilați cu un nivel specific de verbozitate:

`dotnet build --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`

- Compilați pentru o anumită perioadă de execuție:

`dotnet build --runtime {{runtime_identifier}}`

- Specificați directorul de ieșire:

`dotnet build --output {{path/to/directory}}`
