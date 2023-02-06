# dotnet restore

> Helyreállítja a .NET projekt függőségeit és eszközeit. További információ: <https://learn.microsoft.com/dotnet/core/tools/dotnet-restore>.

- Egy .NET projekt vagy megoldás függőségeinek visszaállítása az aktuális könyvtárban:

`dotnet restore`

- Egy .NET projekt vagy megoldás függőségeinek visszaállítása egy adott helyen:

`dotnet restore {{path/to/project_or_solution}}`

- Függőségek visszaállítása a HTTP-kérések gyorsítótárazása nélkül:

`dotnet restore --no-cache`

- Az összes függőség feloldásának kikényszerítése akkor is, ha a legutóbbi visszaállítás sikeres volt:

`dotnet restore --force`

- A függőségek visszaállítása a csomagforrás hibáinak figyelmeztetésként való felhasználásával:

`dotnet restore --ignore-failed-sources`

- Függőségek visszaállítása egy adott szókimondási szinten:

`dotnet restore --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`
