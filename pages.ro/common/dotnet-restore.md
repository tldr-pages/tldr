# dotnet restore

> Restaurează dependențele și instrumentele unui proiect NET.
> Mai multe informaţii: <https://docs.microsoft.com/dotnet/core/tools/dotnet-restore>

- Restaurați dependențele pentru un proiect sau o soluție NET în directorul curent:

`dotnet restore`

- Restaurați dependențele pentru un proiect sau o soluție NET într-o anumită locație:

`dotnet restore {{path/to/project_or_solution}}`

- Restaurați dependențele fără memorarea în cache a solicitărilor HTTP:

`dotnet restore --no-cache`

- Forțați toate dependențele să fie rezolvate chiar dacă ultima restaurare a avut succes:

`dotnet restore --force`

- Restaurați dependențele utilizând eșecurile sursei pachetelor ca avertismente:

`dotnet restore --ignore-failed-sources`

- Restaurați dependențele cu un anumit nivel de verbozitate:

`dotnet restore --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`
