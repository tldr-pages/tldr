# dotnet publish

> Publicați o aplicație NET și dependențele sale într-un director pentru implementare la un sistem de găzduire.
> Mai multe informaţii: <https://docs.microsoft.com/dotnet/core/tools/dotnet-publish>

- Compilarea unui proiect NET în modul de lansare:

`dotnet publish --configuration Release {{path/to/project_file}}`

- Publicați runtime NET Core cu aplicația dvs. pentru runtime specificat:

`dotnet publish --self-contained true --runtime {{runtime_identifier}} {{path/to/project_file}}`

- Împachetați aplicația într-un executabil cu un singur fișier specific platformei:

`dotnet publish --runtime {{runtime_identifier}} -p:PublishSingleFile=true {{path/to/project_file}}`

- Îndepărtați bibliotecile neutilizate pentru a reduce dimensiunea de implementare a unei aplicații:

`dotnet publish --self-contained true --runtime {{runtime_identifier}} -p:PublishTrimmed=true {{path/to/project_file}}`

- Compilarea unui proiect NET fără restaurarea dependențelor:

`dotnet publish --no-restore {{path/to/project_file}}`

- Specificați directorul de ieșire:

`dotnet publish --output {{path/to/directory}} {{path/to/project_file}}`
