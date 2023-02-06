# dotnet publish

> Egy .NET-alkalmazás és függőségeinek közzététele egy könyvtárba, hogy azt egy tárhelyre telepíthesse. További információ: <https://learn.microsoft.com/dotnet/core/tools/dotnet-publish>.

- .NET projekt fordítása kiadási módban:

`dotnet publish --configuration Release {{path/to/project_file}}`

- A .NET Core futtatási időt a megadott futtatási időhöz tartozó alkalmazással együtt közzéteszi:

`dotnet publish --self-contained true --runtime {{runtime_identifier}} {{path/to/project_file}}`

- Csomagolja az alkalmazást egy platformspecifikus egyfájlos futtatható állományba:

`dotnet publish --runtime {{runtime_identifier}} -p:PublishSingleFile=true {{path/to/project_file}}`

- A nem használt könyvtárak levágása az alkalmazás telepítési méretének csökkentése érdekében:

`dotnet publish --self-contained true --runtime {{runtime_identifier}} -p:PublishTrimmed=true {{path/to/project_file}}`

- .NET-projekt fordítása függőségek visszaállítása nélkül:

`dotnet publish --no-restore {{path/to/project_file}}`

- A kimeneti könyvtár megadása:

`dotnet publish --output {{path/to/directory}} {{path/to/project_file}}`
