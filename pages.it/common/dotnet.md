# dotnet

> Strumenti .NET da linea di comando multipiattaforma per .NET Core.
> Alcuni comandi aggiuntivi, come `dotnet build`, hanno la propria documentazione.
> Maggiori informazioni: <https://docs.microsoft.com/dotnet/core/tools>.

- Inizializza un nuovo progetto .NET:

`dotnet new {{nome_abbreviato_template}}`

- Ripristina pacchetti nuget:

`dotnet restore`

- Costruisci ed esegui il progetto .NET nella directory corrente:

`dotnet run`

- Esegui una applicazione dotnet pacchettizzata (solo il runtime è necessario, il resto dei comandi richiedono .NET Core SDK):

`dotnet {{percorso/a/applicazione.dll}}`
