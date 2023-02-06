# dotnet

> Platformokon átívelő .NET parancssori eszközök a .NET Core-hoz. Néhány alparancsnak, mint például a `dotnet build`, saját használati dokumentációja van. További információ: <https://learn.microsoft.com/dotnet/core/tools>.

- Új .NET projekt inicializálása:

`dotnet new {{template_short_name}}`

- NuGet csomagok visszaállítása:

`dotnet restore`

- A .NET projekt építése és végrehajtása az aktuális könyvtárban:

`dotnet run`

- Egy csomagolt dotnet alkalmazás futtatása (csak a futtatási időre van szükség, a többi parancshoz a .NET Core SDK telepítése szükséges):

`dotnet {{path/to/application.dll}}`
