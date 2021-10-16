# dotnet publish

> Opublikuj aplikację .NET i jej zależności w celu wdrożenia na docelowym systemie.
> Więcej informacji: <https://docs.microsoft.com/dotnet/core/tools/dotnet-publish>.

- Opublikuj projekt w konfiguracji wydania:

`dotnet publish --configuration Release {{ścieżka/do/pliku_projektu}}`

- Opublikuj projekt z dołączonym wybranym środowiskiem uruchomieniowym:

`dotnet publish --self-contained true --runtime {{identyfikator_runtime}} {{ścieżka/do/pliku_projektu}}`

- Zapakuj aplikację do pojedyńczego pliku uruchomieniowego dla konkretnej platformy:

`dotnet publish --runtime {{identyfikator_runtime}} -p:PublishSingleFile=true {{ścieżka/do/pliku_projektu}}`

- Pomiń nieużywane biblioteki aby obniżyć rozmiar wdrażanej aplikacji:

`dotnet publish --self-contained true --runtime {{identyfikator_runtime}} -p:PublishTrimmed=true {{ścieżka/do/pliku_projektu}}`

- Kompiluj projekt bez przywracania zależności:

`dotnet publish --no-restore {{ścieżka/do/pliku_projektu}}`

- Wybierz katalog docelowy:

`dotnet publish --output {{ściezka/do/katalogu}} {{ścieżka/do/pliku_projektu}}`
