# dotnet

> Wieloplatformowe narzędzia wiersza polecenia .NET dla platformy .NET Core.
> Niektóre podkomendy takie jak `build` mają osobną dokumentację.
> Więcej informacji: <https://learn.microsoft.com/dotnet/core/tools>.

- Zainicjuj nowy projekt .NET:

`dotnet new {{krótka_nazwa_szablonu}}`

- Przywróć pakiety NuGet:

`dotnet restore`

- Zbuduj i uruchom projekt .NET w bieżącym katalogu:

`dotnet run`

- Uruchom spakowaną aplikację dotnet (wymaga tylko środowiska wykonawczego, pozostałe polecenia wymagają zainstalowanego zestawu .NET Core SDK):

`dotnet {{ścieżka/do/aplikacji.dll}}`
